"""Gera índices do portfólio a partir dos arquivos de ações e projetos."""
from __future__ import annotations

from collections import Counter
from datetime import date
from html import escape
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
ACOES = ROOT / "acoes"
PROJETOS = ROOT / "projetos"
OUT = ROOT / "generated"
MESES = ROOT / "meses"
MONTHS = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]


def fail(message: str) -> None:
    print(f"\nPublicação interrompida: {message}\n", file=sys.stderr)
    raise SystemExit(1)


def qmd_data(path: Path) -> tuple[dict, str]:
    raw = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", raw, re.S)
    if not match:
        fail(f"{path.relative_to(ROOT)} não tem cabeçalho YAML válido.")
    data: dict = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            fail(f"{path.relative_to(ROOT)} tem cabeçalho inválido na linha: {line}")
        key, raw_value = line.split(":", 1)
        key, raw_value = key.strip(), raw_value.strip()
        if raw_value in {"null", ""}:
            value = None
        elif raw_value.startswith("[") and raw_value.endswith("]"):
            value = [item.strip().strip('"\'') for item in raw_value[1:-1].split(",") if item.strip()]
        elif raw_value.startswith('"') and raw_value.endswith('"'):
            value = raw_value[1:-1]
        elif re.fullmatch(r"-?\d+", raw_value):
            value = int(raw_value)
        elif re.fullmatch(r"-?\d+(\.\d+)?", raw_value):
            value = float(raw_value)
        else:
            value = raw_value
        data[key] = value
    return data, match.group(2)


def action_records() -> list[dict]:
    records = []
    for path in sorted(ACOES.glob("*.qmd")):
        if path.name.startswith("_"):
            continue
        data, _ = qmd_data(path)
        required = ["title", "description", "date", "categories", "status"]
        missing = [field for field in required if not data.get(field)]
        if missing:
            fail(f"{path.relative_to(ROOT)} sem campo obrigatório: {', '.join(missing)}.")
        try:
            when = date.fromisoformat(str(data["date"]))
        except ValueError:
            fail(f"{path.relative_to(ROOT)} tem data inválida: {data['date']}.")
        prefix = re.match(r"(\d{4})-(\d{2})-", path.name)
        if not prefix or (int(prefix.group(1)), int(prefix.group(2))) != (when.year, when.month):
            fail(f"{path.relative_to(ROOT)} deve começar por {when:%Y-%m}- para coincidir com date.")
        if data["status"] != "publicado":
            continue
        cats = data["categories"] if isinstance(data["categories"], list) else [data["categories"]]
        records.append({**data, "categories": cats, "when": when, "source": path, "url": f"acoes/{path.stem}.html"})
    return sorted(records, key=lambda r: (r["when"], r.get("ordem") or 999), reverse=True)


def project_records() -> list[dict]:
    records = []
    for path in sorted(PROJETOS.glob("*.qmd")):
        if path.name.startswith("_"):
            continue
        data, _ = qmd_data(path)
        if not data.get("title") or not data.get("description"):
            fail(f"{path.relative_to(ROOT)} precisa de title e description.")
        records.append({**data, "source": path, "url": f"projetos/{path.stem}.html"})
    return records


def link(record: dict, from_dir: Path = ROOT) -> str:
    target = ROOT / record["url"]
    return target.relative_to(from_dir).as_posix() if from_dir == ROOT else Path("..").joinpath(record["url"]).as_posix()


def badges(record: dict) -> str:
    return "".join(f'<span class="tag">{escape(str(category))}</span>' for category in record["categories"])


def action_card(record: dict, from_dir: Path = ROOT) -> str:
    image = record.get("image") or "fotos/hero-workshop-demo.png"
    image_path = image if from_dir == ROOT else "../" + image
    return f'''<article class="action-card">
  <a class="card-image" href="{link(record, from_dir)}"><img src="{escape(image_path)}" alt="{escape(record.get('image-alt') or record['title'])}" loading="lazy"></a>
  <div class="card-body"><div class="card-meta">{record['when'].strftime('%d/%m/%Y')}</div>{badges(record)}
  <h3><a href="{link(record, from_dir)}">{escape(record['title'])}</a></h3><p>{escape(record['description'])}</p></div>
</article>'''


def project_card(record: dict) -> str:
    image = record.get("image")
    image_html = ""
    if image:
        image_html = f'<img class="project-card-image" src="{escape(str(image))}" alt="{escape(str(record.get("image-alt") or record["title"]))}" loading="lazy">'
    label = escape(str(record.get("label") or "Projeto demonstrativo"))
    cta = escape(str(record.get("cta") or "Ver estrutura →"))
    return f'<a class="project-card" href="{record["url"]}">{image_html}<span>{label}</span><h2>{escape(record["title"])}</h2><p>{escape(record["description"])}</p><b>{cta}</b></a>'


def metrics(records: list[dict]) -> dict:
    axes = {c for r in records for c in r["categories"]}
    participants = sum(int(r.get("participantes") or 0) for r in records)
    hours = sum(float(r.get("horas") or 0) for r in records)
    measured = sum(1 for r in records if r.get("participantes") is not None or r.get("horas") is not None)
    return {"actions": len(records), "axes": len(axes), "participants": participants, "hours": hours, "measured": measured, "months": len({(r['when'].year, r['when'].month) for r in records})}


def metric_grid(m: dict) -> str:
    return f'''<div class="metric-grid">
  <div><strong>{m['actions']}</strong><span>ações registradas</span></div><div><strong>{m['months']}</strong><span>meses cobertos</span></div>
  <div><strong>{m['participants']}</strong><span>participações informadas</span></div><div><strong>{m['hours']:g}h</strong><span>horas de formação</span></div>
</div>'''


def write(name: str, content: str) -> None:
    OUT.mkdir(exist_ok=True)
    (OUT / name).write_text(content.strip() + "\n", encoding="utf-8")


def make_month_pages(records: list[dict]) -> None:
    grouped: dict[tuple[int, int], list[dict]] = {}
    for r in records:
        grouped.setdefault((r["when"].year, r["when"].month), []).append(r)
    for (year, month), items in grouped.items():
        filename = f"{year}-{month:02}.qmd"
        body = "\n".join(action_card(r, MESES) for r in items)
        page = f'''---
title: "{MONTHS[month - 1].title()} de {year}"
description: "Ações do NAPED Afya Ipatinga em {MONTHS[month - 1]} de {year}."
---

<div class="page-kicker">Linha do tempo · {year}</div>

<div class="action-grid">{body}</div>
'''
        (MESES / filename).write_text(page, encoding="utf-8")


def make_project_action_lists(records: list[dict], projects: list[dict]) -> None:
    """Gera uma ramificação de ações para cada projeto publicado."""
    for project in projects:
        keys = {str(project["title"]).strip().casefold()}
        if project.get("project-key"):
            keys.add(str(project["project-key"]).strip().casefold())
        related = [r for r in records if str(r.get("projeto") or "").strip().casefold() in keys]
        if related:
            content = '<div class="action-grid">' + "\n".join(action_card(r, PROJETOS) for r in related) + "</div>"
        else:
            content = '<div class="empty-state">Ainda não há ações vinculadas a este projeto.</div>'
        write(f'projeto-{project["source"].stem}.md', content)


def main() -> None:
    records = action_records()
    projects = project_records()
    if not records:
        fail("Não há ações publicadas para gerar o portfólio.")
    m = metrics(records)
    by_month = Counter((r["when"].year, r["when"].month) for r in records)
    by_axis = Counter(c for r in records for c in r["categories"])
    write("home.md", metric_grid(m))
    write("recentes.md", '<div class="action-grid">' + "\n".join(action_card(r) for r in records[:3]) + "</div>")
    write("acoes.md", '<div class="action-grid">' + "\n".join(action_card(r) for r in records) + "</div>")
    month_items = "".join(f'<li><a href="meses/{year}-{month:02}.html"><strong>{MONTHS[month-1].title()} de {year}</strong><span>{count} ações</span><b>Ver ações →</b></a></li>' for (year, month), count in sorted(by_month.items()))
    write("meses.md", '<ul class="month-list">' + month_items + "</ul>")
    project_cards = "".join(project_card(p) for p in projects)
    write("projetos.md", '<div class="project-grid">' + project_cards + "</div>")
    bars = "".join(f'<div class="bar-row"><span>{escape(axis)}</span><i style="width:{count / max(by_axis.values()) * 100:.0f}%"></i><b>{count}</b></div>' for axis, count in by_axis.most_common())
    rows = "".join(f'<tr><td>{r["when"].strftime("%d/%m/%Y")}</td><td><a href="{r["url"]}">{escape(r["title"])}</a></td><td>{escape(", ".join(r["categories"]))}</td><td>{escape(str(r.get("publico") or "—"))}</td></tr>' for r in records)
    write("resultados.md", metric_grid(m) + f'<h2>Volume por eixo</h2><div class="bar-chart">{bars}</div><p class="coverage-note">Indicadores de participação e horas cobrem {m["measured"]} de {m["actions"]} ações demonstrativas. Uma ação pode pertencer a mais de um eixo.</p><h2>Todas as ações</h2><div class="table-wrap"><table><thead><tr><th>Data</th><th>Ação</th><th>Eixos</th><th>Público</th></tr></thead><tbody>{rows}</tbody></table></div>')
    sdd = next((r for r in records if r["source"].stem == "2026-07-sdd-semana-desenvolvimento-docente"), None)
    if sdd is None:
        fail("A ação da SDD de 01/07/2026 não foi encontrada para gerar as comprovações.")
    evidence = f'<article class="evidence-card"><span>Lista de presença · 01/07/2026</span><h2>{escape(sdd["title"])}</h2><p>Registro de participação da programação da Semana de Desenvolvimento Docente realizada em 01/07/2026.</p><a href="{sdd["url"]}">Abrir ação →</a></article>'
    write("comprovacoes.md", '<div class="evidence-grid">' + evidence + "</div>")
    for semester, filename in ((1, "2026-1.md"), (2, "2026-2.md")):
        subset = [r for r in records if (r["when"].month <= 6) == (semester == 1)]
        sm = metrics(subset)
        write(filename, metric_grid(sm) + '<div class="action-grid">' + "\n".join(action_card(r, ROOT / "em-numeros") for r in subset) + "</div>")
    make_month_pages(records)
    make_project_action_lists(records, projects)
    print(f"Gerados {len(records)} registros, {len(projects)} projetos e {len(by_month)} páginas mensais.")


if __name__ == "__main__":
    main()
