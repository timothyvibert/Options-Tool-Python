# Report v2 HTML/CSS Renderer (WeasyPrint)

## Install (Windows + conda)
Preferred path (handles native dependencies cleanly):

```bash
conda install -c conda-forge weasyprint jinja2
```

## Install (pip)
If you use pip, be aware WeasyPrint may require native system libraries on Windows.

```bash
pip install weasyprint jinja2
```

## Render a sample PDF
```bash
python tools/render_report_html_v2.py --contract Design/sample_report_contract.json --out out/report_html_v2.pdf
```
