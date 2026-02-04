from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, Mapping, Optional

from reporting.contract_v1.adapter import build_report_contract_v1
from reporting.contract_v1.validate import validate_report_contract_v1
from reporting.html_v2.view_model import build_view_model


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


def _configure_fontconfig() -> None:
    prefix = os.environ.get("CONDA_PREFIX")
    if not prefix:
        return
    fonts_dir = Path(prefix) / "etc" / "fonts"
    fonts_conf = fonts_dir / "fonts.conf"
    if "FONTCONFIG_PATH" not in os.environ and fonts_dir.exists():
        os.environ["FONTCONFIG_PATH"] = str(fonts_dir)
    if "FONTCONFIG_FILE" not in os.environ and fonts_conf.exists():
        os.environ["FONTCONFIG_FILE"] = str(fonts_conf)
    if os.environ.get("REPORT_HTML_DEBUG") == "1":
        print(
            "report_html_debug: FONTCONFIG_PATH="
            f"{os.environ.get('FONTCONFIG_PATH')} exists={fonts_dir.exists()}"
        )
        print(
            "report_html_debug: FONTCONFIG_FILE="
            f"{os.environ.get('FONTCONFIG_FILE')} exists={fonts_conf.exists()}"
        )


def _load_css(repo_root: Path) -> str:
    css_path = repo_root / "reporting" / "html_v2" / "assets" / "print.css"
    if not css_path.exists():
        raise RuntimeError(f"Missing print stylesheet: {css_path}")
    return css_path.read_text(encoding="utf-8")


def _is_contract_v1(data: Mapping[str, object]) -> bool:
    meta = data.get("meta")
    if isinstance(meta, Mapping):
        return meta.get("report_version") == "v1"
    return False


def build_report_pdf_html(report_model: Mapping[str, object], *, out_path: Optional[str] = None) -> bytes:
    _configure_fontconfig()
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
    if _is_contract_v1(model):
        contract = model
    else:
        contract = build_report_contract_v1(model)
    validate_report_contract_v1(contract)
    context = build_view_model(contract)
    template_dir = Path(__file__).resolve().parent / "templates"
    css_text = _load_css(repo_root)

    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("base.html")
    html_text = template.render(report=context, css=css_text)

    if os.environ.get("REPORT_HTML_DEBUG") == "1":
        debug_dir = repo_root / "out"
        debug_dir.mkdir(parents=True, exist_ok=True)
        debug_path = debug_dir / "report_debug.html"
        debug_path.write_text(html_text, encoding="utf-8")

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
