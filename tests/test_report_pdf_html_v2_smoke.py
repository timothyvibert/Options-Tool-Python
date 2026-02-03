import io
import json
from pathlib import Path

import pytest

from reporting.html_v2.renderer import build_report_pdf_html


def test_report_pdf_html_v2_smoke():
    pytest.importorskip("weasyprint")
    pytest.importorskip("jinja2")

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

    assert pdf_bytes.startswith(b"%PDF")
    assert b"%%EOF" in pdf_bytes[-2048:]

    pdf_reader = None
    try:
        from pypdf import PdfReader as _PdfReader  # type: ignore
    except Exception:
        _PdfReader = None
    if _PdfReader is None:
        try:
            from PyPDF2 import PdfReader as _PdfReader  # type: ignore
        except Exception:
            _PdfReader = None
    if _PdfReader is not None:
        pdf_reader = _PdfReader(io.BytesIO(pdf_bytes))
        assert len(pdf_reader.pages) >= 1
