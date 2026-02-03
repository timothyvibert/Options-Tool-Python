from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from reporting.html_v2.renderer import build_report_pdf_html


def _default_contract_path() -> Path:
    return Path(__file__).resolve().parents[1] / "Design" / "sample_report_contract.json"


def main() -> None:
    parser = argparse.ArgumentParser(description="Render report v2 HTML/CSS PDF (WeasyPrint).")
    parser.add_argument(
        "--contract",
        default=str(_default_contract_path()),
        help="Path to a report_model JSON contract.",
    )
    parser.add_argument(
        "--out",
        default="out/report_html_v2.pdf",
        help="Output PDF path.",
    )
    args = parser.parse_args()

    contract_path = Path(args.contract)
    if not contract_path.exists():
        raise SystemExit(f"Contract not found: {contract_path}")

    report_model = json.loads(contract_path.read_text(encoding="utf-8"))
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    pdf_bytes = build_report_pdf_html(report_model, out_path=str(out_path))
    print(f"OK: wrote {out_path} ({len(pdf_bytes)} bytes)")


if __name__ == "__main__":
    main()
