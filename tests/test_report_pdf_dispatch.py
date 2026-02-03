from pathlib import Path

import pytest

from reporting import report_pdf
import reporting.html_v2.renderer as html_renderer


def test_build_client_report_pdf_prefers_html(monkeypatch):
    pytest.importorskip("weasyprint")
    sentinel = b"%PDF-FAKE\n%%EOF"

    def _fake_html(_model):
        return sentinel

    def _fake_reportlab(path, report_model, logo_path=None):
        Path(path).write_bytes(b"%PDF-REPORTLAB\n%%EOF")

    monkeypatch.setattr(html_renderer, "build_report_pdf_html", _fake_html)
    monkeypatch.setattr(report_pdf, "build_report_pdf_v2", _fake_reportlab)

    result = report_pdf.build_client_report_pdf({"header": {}}, prefer_html=True)
    assert result == sentinel


def test_build_client_report_pdf_fallback(monkeypatch):
    def _boom(_model):
        raise RuntimeError("boom")

    def _fake_reportlab(path, report_model, logo_path=None):
        Path(path).write_bytes(b"%PDF-REPORTLAB\n%%EOF")

    monkeypatch.setattr(html_renderer, "build_report_pdf_html", _boom)
    monkeypatch.setattr(report_pdf, "build_report_pdf_v2", _fake_reportlab)

    result = report_pdf.build_client_report_pdf({"header": {}}, prefer_html=True)
    assert result.startswith(b"%PDF")
