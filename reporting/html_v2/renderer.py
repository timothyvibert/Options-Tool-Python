from __future__ import annotations

import base64
import os
import platform
from pathlib import Path
from typing import Any, Dict, Mapping, Optional


def _fix_pango_dll() -> None:
    """Fix WeasyPrint Pango DLL discovery on Windows conda environments."""
    if platform.system() != "Windows":
        return

    conda_prefix = os.environ.get("CONDA_PREFIX", "")
    if not conda_prefix:
        return

    lib_bin = os.path.join(conda_prefix, "Library", "bin")
    if not os.path.isdir(lib_bin):
        return

    # Add to DLL search path (Python 3.8+)
    try:
        os.add_dll_directory(lib_bin)
    except (OSError, AttributeError):
        pass

    # Also add to PATH as fallback
    if lib_bin not in os.environ.get("PATH", ""):
        os.environ["PATH"] = lib_bin + os.pathsep + os.environ.get("PATH", "")

    # Create copies for lib-prefixed names if they don't exist
    for dll in os.listdir(lib_bin):
        if dll.endswith(".dll") and not dll.startswith("lib"):
            lib_name = "lib" + dll
            lib_path = os.path.join(lib_bin, lib_name)
            if not os.path.exists(lib_path):
                try:
                    import shutil
                    shutil.copy2(os.path.join(lib_bin, dll), lib_path)
                except (OSError, PermissionError):
                    pass


_fix_pango_dll()

from reporting.contract_v1.adapter import build_report_contract_v1
from reporting.contract_v1.validate import validate_report_contract_v1
from reporting.html_v2.view_model import build_payoff_chart_png_data_uri, build_view_model


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


def _coerce_float(value: object) -> Optional[float]:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        text = value.strip().replace(",", "").replace("%", "")
        if not text:
            return None
        try:
            return float(text)
        except ValueError:
            return None
    return None


def _coerce_series(values: object) -> Optional[list[float]]:
    if not isinstance(values, list) or not values:
        return None
    series: list[float] = []
    for value in values:
        num = _coerce_float(value)
        if num is None:
            return None
        series.append(num)
    return series


def _svg_placeholder() -> str:
    width = 640
    height = 320
    return (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {width} {height}'>"
        "<rect width='100%' height='100%' fill='white'/>"
        "<line x1='48' y1='24' x2='48' y2='288' stroke='#e5e7eb' stroke-width='1'/>"
        "<line x1='48' y1='288' x2='608' y2='288' stroke='#e5e7eb' stroke-width='1'/>"
        "<text x='320' y='170' text-anchor='middle' fill='#6b7280' font-size='12'>Payoff Diagram</text>"
        "</svg>"
    )


def _build_payoff_svg_data_uri(model: Mapping[str, object]) -> str:
    payoff = model.get("payoff") if isinstance(model.get("payoff"), Mapping) else None
    x_values = _coerce_series(payoff.get("price_grid")) if payoff else None
    stock_values = _coerce_series(payoff.get("stock_pnl")) if payoff else None
    options_values = _coerce_series(payoff.get("options_pnl")) if payoff else None
    combined_values = _coerce_series(payoff.get("combined_pnl")) if payoff else None

    if not (x_values and stock_values and options_values and combined_values):
        data = base64.b64encode(_svg_placeholder().encode("utf-8")).decode("ascii")
        return f"data:image/svg+xml;base64,{data}"

    min_len = min(len(x_values), len(stock_values), len(options_values), len(combined_values))
    x = x_values[:min_len]
    stock = stock_values[:min_len]
    options = options_values[:min_len]
    combined = combined_values[:min_len]

    min_x, max_x = min(x), max(x)
    min_y = min(min(stock), min(options), min(combined), 0.0)
    max_y = max(max(stock), max(options), max(combined), 0.0)
    if min_x == max_x:
        min_x -= 1.0
        max_x += 1.0
    if min_y == max_y:
        min_y -= 1.0
        max_y += 1.0

    width = 640.0
    height = 320.0
    pad_left = 48.0
    pad_right = 32.0
    pad_top = 24.0
    pad_bottom = 32.0
    plot_w = width - pad_left - pad_right
    plot_h = height - pad_top - pad_bottom

    def sx(value: float) -> float:
        return pad_left + (value - min_x) / (max_x - min_x) * plot_w

    def sy(value: float) -> float:
        return pad_top + (max_y - value) / (max_y - min_y) * plot_h

    def polyline(points: list[tuple[float, float]], stroke: str, dash: Optional[str] = None) -> str:
        pts = " ".join(f"{sx(px):.2f},{sy(py):.2f}" for px, py in points)
        dash_attr = f" stroke-dasharray='{dash}'" if dash else ""
        return (
            f"<polyline points='{pts}' fill='none' stroke='{stroke}' stroke-width='2'{dash_attr} />"
        )

    grid_lines = []
    for step in (0.25, 0.5, 0.75):
        y = pad_top + plot_h * step
        grid_lines.append(
            f"<line x1='{pad_left:.2f}' y1='{y:.2f}' x2='{pad_left + plot_w:.2f}' "
            f"y2='{y:.2f}' stroke='#f3f4f6' stroke-width='1' />"
        )

    axis_y = sy(0.0)
    axis_y = max(pad_top, min(axis_y, pad_top + plot_h))
    axis_line = (
        f"<line x1='{pad_left:.2f}' y1='{axis_y:.2f}' x2='{pad_left + plot_w:.2f}' "
        f"y2='{axis_y:.2f}' stroke='#e5e7eb' stroke-width='1' />"
    )
    axis_x = (
        f"<line x1='{pad_left:.2f}' y1='{pad_top:.2f}' x2='{pad_left:.2f}' "
        f"y2='{pad_top + plot_h:.2f}' stroke='#e5e7eb' stroke-width='1' />"
    )

    svg_parts = [
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {width:.0f} {height:.0f}'>",
        "<rect width='100%' height='100%' fill='white'/>",
        *grid_lines,
        axis_line,
        axis_x,
        polyline(list(zip(x, stock)), "#93c5fd"),
        polyline(list(zip(x, options)), "#c4b5fd"),
        polyline(list(zip(x, combined)), "#4b5563", dash="4,3"),
        "</svg>",
    ]
    svg = "".join(svg_parts)
    data = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return f"data:image/svg+xml;base64,{data}"


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
    css_path = repo_root / "reporting" / "html_v2" / "assets" / "figma_v2_print.css"
    if not css_path.exists():
        raise RuntimeError(f"Missing print stylesheet: {css_path}")
    return css_path.read_text(encoding="utf-8")


def _load_ubs_logo_data_uri(repo_root: Path) -> str:
    candidates = [
        repo_root / "Design" / "UBS Logo Png.png",
        repo_root / "Design" / "UBS Logo.png",
    ]
    for path in candidates:
        if path.exists():
            data = base64.b64encode(path.read_bytes()).decode("ascii")
            return f"data:image/png;base64,{data}"
    return ""


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
    payoff_svg = build_payoff_chart_png_data_uri(model)
    if _is_contract_v1(model):
        contract = model
    else:
        contract = build_report_contract_v1(model)
    validate_report_contract_v1(contract)
    context = build_view_model(contract)
    template_dir = Path(__file__).resolve().parent / "templates"
    css_text = _load_css(repo_root)
    assets = {
        "ubs_logo_data_uri": _load_ubs_logo_data_uri(repo_root),
        "payoff_chart_data_uri": payoff_svg,
    }

    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("base.html")
    html_text = template.render(report=context, css=css_text, assets=assets)

    if os.environ.get("REPORT_HTML_DEBUG") == "1":
        debug_dir = repo_root / "out"
        debug_dir.mkdir(parents=True, exist_ok=True)
        debug_html_path = debug_dir / "report_debug.html"
        debug_html_path.write_text(html_text, encoding="utf-8")
        debug_css_path = debug_dir / "report_debug.css"
        debug_css_path.write_text(css_text, encoding="utf-8")
        print(f"report_html_debug: wrote {debug_html_path}")
        print(f"report_html_debug: wrote {debug_css_path}")

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
