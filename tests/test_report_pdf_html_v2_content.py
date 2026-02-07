import io
import json
from pathlib import Path

import pytest

from reporting.html_v2.renderer import build_report_pdf_html


def _load_pdf_reader():
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception:
        try:
            from PyPDF2 import PdfReader  # type: ignore
        except Exception:
            return None
    return PdfReader


def test_html_v2_header_text():
    pytest.importorskip("weasyprint")
    pytest.importorskip("jinja2")

    pdf_reader_cls = _load_pdf_reader()
    if pdf_reader_cls is None:
        pytest.skip("pypdf/PyPDF2 not available")

    repo_root = Path(__file__).resolve().parents[1]
    contract_path = repo_root / "Design" / "sample_report_contract.json"
    report_model = json.loads(contract_path.read_text(encoding="utf-8"))

    try:
        pdf_bytes = build_report_pdf_html(report_model)
    except RuntimeError as exc:
        message = str(exc)
        if "system libraries are missing" in message:
            pytest.skip(message)
        raise

    reader = pdf_reader_cls(io.BytesIO(pdf_bytes))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)

    assert "Wealth Management Option Strategy" in text
    assert "Scenario Analysis" in text
    assert "Option Strategy Details" in text

    strategy = report_model.get("header", {}).get("strategy_name")
    if isinstance(strategy, str) and strategy.strip():
        assert text.count(strategy.strip()) >= 2
