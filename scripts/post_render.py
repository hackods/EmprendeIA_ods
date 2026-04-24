"""
Post-render hook — mueve docs/dashboard/index.{html,_files} a docs/index.{html,_files}.

La rúbrica HackODS pide tanto `dashboard/index.qmd` (T2) como `docs/index.html` (T4).
Quarto en modo `default` preserva la estructura del input, produciendo
`docs/dashboard/index.html`. Este script aplana esa ruta.
"""
from pathlib import Path
import shutil

DOCS = Path("docs")
src_html = DOCS / "dashboard" / "index.html"
src_files = DOCS / "dashboard" / "index_files"

if not src_html.exists():
    raise SystemExit(f"post_render: no existe {src_html}")

dst_html = DOCS / "index.html"
dst_files = DOCS / "index_files"

if dst_files.exists():
    shutil.rmtree(dst_files)
if src_files.exists():
    shutil.copytree(src_files, dst_files)

shutil.copy2(src_html, dst_html)
print(f"post_render: {src_html} -> {dst_html}")
