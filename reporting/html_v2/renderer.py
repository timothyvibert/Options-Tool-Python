from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Mapping, Optional

from reporting.html_v2.view_model import build_view_model_from_contract


def _ensure_dict(report_model: object) -> Dict[str, Any]:
    if isinstance(report_model, dict):
        return report_model
    to_dict = getattr(report_model, "to_dict", None)
    if callable(to_dict):
        try:
            return to_dict()
        except Exception:
            pass
    raw = getattr(report_model, "__dict__", None)
    if isinstance(raw, dict):
        return dict(raw)
    return {}


def _load_css(repo_root: Path) -> str:
    design_root = repo_root / "Design" / "figma_report_v2" / "src"
    index_css = design_root / "index.css"
    globals_css = design_root / "styles" / "globals.css"
    if not index_css.exists() or not globals_css.exists():
        raise RuntimeError(
            "Missing Design CSS files. Expected: "
            f"{globals_css} and {index_css}."
        )
    css_text = globals_css.read_text(encoding="utf-8")
    css_text += "\n" + index_css.read_text(encoding="utf-8")
    css_text += (
        "\n@page { size: 8.5in 11in; margin: 0; }\n"
        "@media print { body { print-color-adjust: exact; -webkit-print-color-adjust: exact; } }\n"
    )
    return css_text


def build_report_pdf_html(report_model: Mapping[str, object], *, out_path: Optional[str] = None) -> bytes:
    try:
        from jinja2 import Environment, FileSystemLoader, select_autoescape
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise RuntimeError(
            "Jinja2 not installed. Install via conda or pip (e.g., conda install jinja2)."
        ) from exc

    try:
        from weasyprint import HTML
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise RuntimeError(
            "WeasyPrint not installed. Install via conda or pip (e.g., conda install weasyprint)."
        ) from exc

    repo_root = Path(__file__).resolve().parents[2]
    model = _ensure_dict(report_model)
    context = build_view_model_from_contract(model)
    template_dir = Path(__file__).resolve().parent / "templates"
    css_text = _load_css(repo_root)

    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("base.html")
    html_text = template.render(report=context, css=css_text)

    base_url = str(repo_root)
    html = HTML(string=html_text, base_url=base_url)
    try:
        pdf_bytes = html.write_pdf()
    except (OSError, RuntimeError) as exc:  # pragma: no cover - environment dependent
        raise RuntimeError(
            "WeasyPrint installed but required system libraries are missing on Windows. "
            "Recommended conda install: conda install -c conda-forge weasyprint jinja2."
        ) from exc

    if out_path:
        Path(out_path).write_bytes(pdf_bytes)
    return pdf_bytes
