# Options Tool (Streamlit + Bloomberg + PDF)

## Non-negotiables
- /core must be pure deterministic logic (no Streamlit, no Bloomberg, no PDF imports).
- Every change in /core must include pytest unit tests.
- Default behavior must match the Excel v1 expiry-payoff engine; improvements must be behind toggles.

## Commands
- Run tests: pytest -q
- Run app: streamlit run app/streamlit_app.py
