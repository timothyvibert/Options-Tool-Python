# Report v2 Template Renderer (Design/src CLI)

This provides a proof-of-render path using the existing Design/src template.
It is NOT wired into Dash yet.

## Prereqs
- Node.js (LTS recommended)
- npm (or pnpm/yarn, matching the Design/figma_report_v2 package)

## Install
```bash
cd Design/figma_report_v2
npm install
```

If Playwright browser binaries are not installed:
```bash
npx playwright install chromium
```

## Generate a deterministic contract JSON
```bash
python tools/build_report_contract_json.py
```

This writes:
```
Design/sample_report_contract.json
```

## Render the PDF from the template
```bash
node Design/figma_report_v2/src/cli/render_report.mjs \
  Design/sample_report_contract.json \
  Design/out/report_v2_template.pdf
```

Output:
```
Design/out/report_v2_template.pdf
```

## Notes
- The renderer uses the existing StrategyReport template.
- The JSON contract is produced via reporting.report_model and mapped into the template shape.
- This CLI is a proof step; Dash wiring remains unchanged.
