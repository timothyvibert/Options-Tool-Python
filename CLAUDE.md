# CLAUDE.md — Alpha Engine (Options Strategy Builder)

## What this project is
An institutional-grade options strategy platform for the UBS Equities & Options Sales desk.
It pulls data from Bloomberg, computes options strategy payoffs and scenarios, visualizes them
in a Dash web UI, and generates a client-ready 2-page PDF report matching a Figma design template.

## Entrypoints (use these, not legacy scripts)
- **Run app**: `python -m frontend_dash.run_vnext`
- **Run tests**: `python -m pytest -q`
- **Render HTML report from sample contract**: `python tools/render_report_html_v2.py --contract Design/sample_report_contract.json --out out/report_html_v2.pdf`
- **Build sample contract JSON**: `python tools/build_report_contract_json.py`

## Environment
- OS: Windows
- Python: 3.13.x (conda env: "options-tool")
- Activate: `conda activate options-tool`
- Key deps: Dash 2.18.x, ReportLab 4.4.x, WeasyPrint (conda-forge), Jinja2, jsonschema

## Architecture (data flows top to bottom — never reverse)
```
User inputs (Dash UI)
  → core.analysis_pack.build_analysis_pack()    [deterministic computation]
  → reporting.report_model.build_report_model()  [normalize to dict]
  → reporting.contract_v1.adapter.build_report_contract_v1()  [strict contract]
  → reporting.contract_v1.validate.validate_report_contract_v1()  [schema check]
  → reporting.html_v2.renderer.build_report_pdf_html()  [Jinja2 + WeasyPrint → PDF]
  → (silent fallback: reporting.report_pdf ReportLab if HTML fails)
```

## Non-negotiable rules
1. **Core purity**: `core/` has no UI, no Bloomberg, no PDF imports. Changes to core/ require tests.
2. **No recomputation in reporting**: Report generation consumes cached analysis_pack only. Never triggers Bloomberg or re-runs analysis.
3. **HTML/WeasyPrint is default renderer**. ReportLab is silent fallback only. Do not extend ReportLab.
4. **Contract-first rendering**: contract_v1 drives all visibility, computed/not_computed status, and field values. Renderers are "dumb" — they format, they do not infer business meaning.
5. **No runtime JS/Node/Playwright/Kaleido**: The PDF pipeline must be pure Python at runtime. Dev-time tooling to generate static CSS artifacts is acceptable if committed to the repo.
6. **Bloomberg boundaries**: Spot lookup only on ticker commit (blur/enter). Market refresh only on explicit "Refresh Data". No Bloomberg calls from dropdown changes, UI toggles, or report generation.
7. **One change at a time**: Make a single PR-sized change, run tests, validate manually, then move on.

## Report design
- **Figma source of truth**: `Design/figma_report_v2/2026-01-18 figma test client report v2.pdf`
- **Design spec**: `Design/REPORT_SPEC.md`
- **HTML template export**: `Design/figma_report_v2/figma_HTML_report_template.html`
  - This uses Tailwind CDN+JS which WeasyPrint cannot execute
  - Must be converted to static CSS for WeasyPrint compatibility
- **Sample contract**: `Design/sample_report_contract.json`
- **Gap analysis**: `reporting/CLIENT_REPORT_V2_GAP_ANALYSIS.md`

## Current state and priorities
The Dash app launches and mostly works. The PDF report generates but has visual fidelity issues
compared to the Figma template.

### Sprint 1 (NOW): Template Fidelity Lock
Goal: Make generated PDF visually match Figma using the exported HTML template as base markup.
- Wire reporting/html_v2 to use figma_HTML_report_template.html as the base
- Replace Tailwind CDN with committed static CSS (WeasyPrint-safe)
- Jinja-wire the template with contract_v1 variables
- 2-page layout with correct page breaks, margins, banner alignment
- Debug artifact: emit report_debug.html behind REPORT_HTML_DEBUG=1 env var

### Sprint 2: Data Completeness
- Fill missing contract fields from analysis_pack
- Fix field mappings (risk/reward, scenario move_pct, strategy descriptions)
- Client position visibility when shares=0

### Sprint 3: Performance
- Fast PDF generation (reduce CSS complexity, avoid expensive WeasyPrint constructs)

### Sprint 4: UI Modernization (DMC)
- Replace ad-hoc Dash HTML with Dash Mantine Components

## Directory structure (key areas)
- `core/` — Deterministic analytics engine (payoff, scenarios, ROI, margin, narrative)
- `adapters/` — Bloomberg and Excel adapters
- `frontend_dash/` — Dash vNext UI (layout, callbacks)
- `reporting/` — Report model, contract_v1, HTML v2 renderer, ReportLab fallback
- `Design/` — Figma assets, spec, sample contracts, logos
- `tests/` — Unit and integration tests
- `tools/` — CLI utilities
- `data/` — CSV strategy maps
- `out/` — Local outputs (not committed)

## Testing
- Always run `python -m pytest -q` after changes
- Report tests check: page count, disclaimer presence on page 2, header on page 1
- Core tests enforce deterministic computation matches Excel baseline

## Git conventions
- Commit messages: `type(scope): description` (e.g., `fix(report): stabilize page 2 layout`)
- Types: feat, fix, refactor, test, docs, chore
- Do not commit: out/, node_modules/, __pycache__/, .env
