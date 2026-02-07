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


def _build_pdf_and_reader():
    """Shared helper: build PDF from sample contract, return (reader, report_model)."""
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
    return reader, report_model


def test_html_v2_header_text():
    reader, report_model = _build_pdf_and_reader()
    text = "\n".join(page.extract_text() or "" for page in reader.pages)

    assert "Wealth Management Option Strategy" in text
    assert "Scenario Analysis" in text
    assert "Option Strategy Details" in text

    strategy = report_model.get("header", {}).get("strategy_name")
    if isinstance(strategy, str) and strategy.strip():
        assert text.count(strategy.strip()) >= 2


def test_html_v2_pdf_has_two_pages():
    reader, _ = _build_pdf_and_reader()
    assert len(reader.pages) == 2, f"Expected 2 pages, got {len(reader.pages)}"


def test_html_v2_page1_contains_strategy_title():
    reader, report_model = _build_pdf_and_reader()
    page1_text = reader.pages[0].extract_text() or ""
    strategy = report_model.get("header", {}).get("strategy_name", "")
    if isinstance(strategy, str) and strategy.strip():
        assert strategy.strip() in page1_text, (
            f"Strategy title '{strategy}' not found on page 1"
        )
    assert "Wealth Management Option Strategy" in page1_text


def test_html_v2_page2_contains_disclosures():
    reader, _ = _build_pdf_and_reader()
    page2_text = reader.pages[1].extract_text() or ""
    assert "Important Risk Disclosures" in page2_text or "Disclosures" in page2_text, (
        "Page 2 should contain disclosure text"
    )


def test_html_v2_page1_contains_short_disclaimer():
    reader, _ = _build_pdf_and_reader()
    page1_text = reader.pages[0].extract_text() or ""
    assert "illustration" in page1_text.lower() or "informational" in page1_text.lower() or "Options" in page1_text, (
        "Page 1 should contain the short header disclaimer"
    )
