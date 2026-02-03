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
        repo_root = Path(__file__).resolve().parents[1]
        alt_paths = [
            repo_root / "Design" / "sample_report_contract.json",
            repo_root / "Design" / "figma_report_v2" / "Design" / "sample_report_contract.json",
        ]
        locations = "\n".join(str(path) for path in alt_paths)
        raise SystemExit(
            "Contract not found. Expected one of:\n"
            f"{locations}"
        )

    report_model = json.loads(contract_path.read_text(encoding="utf-8"))
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    pdf_bytes = build_report_pdf_html(report_model, out_path=str(out_path))
    print(f"OK: wrote {out_path} ({len(pdf_bytes)} bytes)")


if __name__ == "__main__":
    main()
