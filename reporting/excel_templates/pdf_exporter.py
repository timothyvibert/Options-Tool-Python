"""Export filled Excel templates to PDF using win32com (Excel COM automation).

Requires:
- Windows OS
- Microsoft Excel installed
- pywin32 (pip install pywin32)
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Optional


def export_pdf(
    xlsx_path: str,
    pdf_path: Optional[str] = None,
    output_sheet: Optional[str] = None,
    visible: bool = False,
    timeout_seconds: int = 30,
) -> str:
    """Open Excel, recalculate formulas, export the output sheet as PDF.

    Args:
        xlsx_path: Path to the filled .xlsx file
        pdf_path: Output PDF path. If None, uses same name as xlsx with .pdf
        output_sheet: Name of sheet to export. If None, exports active sheet.
        visible: If True, show Excel window (useful for debugging)
        timeout_seconds: Max time to wait for Excel operations

    Returns:
        Path to the exported PDF file.

    Raises:
        ImportError: If win32com is not available
        FileNotFoundError: If xlsx_path doesn't exist
        RuntimeError: If Excel COM automation fails
    """
    try:
        import pythoncom
        import win32com.client
    except ImportError:
        raise ImportError(
            "win32com is required for Excel PDF export. "
            "Install with: pip install pywin32"
        )

    xlsx_path = os.path.abspath(xlsx_path)
    if not os.path.exists(xlsx_path):
        raise FileNotFoundError(f"Excel file not found: {xlsx_path}")

    if pdf_path is None:
        pdf_path = os.path.splitext(xlsx_path)[0] + ".pdf"
    pdf_path = os.path.abspath(pdf_path)

    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    excel = None
    wb = None
    try:
        pythoncom.CoInitialize()

        excel = win32com.client.DispatchEx("Excel.Application")
        excel.Visible = visible
        excel.DisplayAlerts = False
        excel.ScreenUpdating = False

        wb = excel.Workbooks.Open(xlsx_path)

        # Force full recalculation (makes all formulas recompute)
        wb.Application.CalculateFull()

        if output_sheet:
            try:
                ws = wb.Sheets(output_sheet)
                ws.Select()
            except Exception as e:
                print(f"[PDF_EXPORT] Warning: could not select sheet '{output_sheet}': {e}")

        # xlTypePDF = 0, xlQualityStandard = 0
        wb.ExportAsFixedFormat(
            Type=0,
            Filename=pdf_path,
            Quality=0,
            IncludeDocProperties=True,
            IgnorePrintAreas=False,
            OpenAfterPublish=False,
        )

        print(f"[PDF_EXPORT] Exported: {pdf_path}")
        return pdf_path

    except Exception as e:
        raise RuntimeError(f"Excel PDF export failed: {e}") from e

    finally:
        try:
            if wb is not None:
                wb.Close(SaveChanges=False)
        except Exception:
            pass
        try:
            if excel is not None:
                excel.Quit()
        except Exception:
            pass
        try:
            pythoncom.CoUninitialize()
        except Exception:
            pass
