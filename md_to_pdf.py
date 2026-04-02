#!/usr/bin/env python3
"""
Convert MIDTERM_PROJECT_PROPOSAL.md to PDF.

Usage:
  python md_to_pdf.py

Options:
  1. If weasyprint is installed: generates PDF directly
  2. Otherwise: generates HTML and opens in browser - use Ctrl+P > Save as PDF
"""

import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
MD_FILE = SCRIPT_DIR / "MIDTERM_PROJECT_PROPOSAL.md"
HTML_FILE = SCRIPT_DIR / "MIDTERM_PROJECT_PROPOSAL.html"
PDF_FILE = SCRIPT_DIR / "MIDTERM_PROJECT_PROPOSAL.pdf"


def main():
    if not MD_FILE.exists():
        print(f"Error: {MD_FILE} not found.")
        sys.exit(1)

    md_content = MD_FILE.read_text(encoding="utf-8")

    # Convert markdown to HTML
    try:
        import markdown
        html_body = markdown.markdown(
            md_content,
            extensions=["tables", "fenced_code", "toc"],
            extension_configs={"toc": {"permalink": True}},
        )
    except ImportError:
        print("Installing markdown package...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown", "-q"])
        import markdown
        html_body = markdown.markdown(
            md_content,
            extensions=["tables", "fenced_code"],
        )

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Midterm Project Proposal - EEG Alzheimer's Detection</title>
  <style>
    body {{ font-family: Georgia, serif; max-width: 800px; margin: 2em auto; padding: 0 2em; line-height: 1.6; color: #333; }}
    h1 {{ border-bottom: 2px solid #333; padding-bottom: 0.3em; }}
    h2 {{ margin-top: 1.5em; color: #444; }}
    h3 {{ margin-top: 1.2em; }}
    table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
    th, td {{ border: 1px solid #ccc; padding: 0.5em 0.75em; text-align: left; }}
    th {{ background: #f5f5f5; font-weight: 600; }}
    code {{ background: #f5f5f5; padding: 0.2em 0.4em; border-radius: 3px; font-size: 0.9em; }}
    pre {{ background: #f5f5f5; padding: 1em; overflow-x: auto; border-radius: 4px; }}
    hr {{ border: none; border-top: 1px solid #ddd; margin: 2em 0; }}
    @media print {{ body {{ max-width: none; }} }}
  </style>
</head>
<body>
{html_body}
</body>
</html>
"""

    HTML_FILE.write_text(html_template, encoding="utf-8")
    print(f"Generated: {HTML_FILE}")

    # Try WeasyPrint for direct PDF (requires GTK/Pango on Windows - often not installed)
    try:
        from weasyprint import HTML
        HTML(string=html_template, base_url=str(SCRIPT_DIR)).write_pdf(PDF_FILE)
        print(f"Generated: {PDF_FILE}")
        return
    except (ImportError, OSError):
        pass

    # Fallback: open HTML in browser for manual print-to-PDF
    import webbrowser
    webbrowser.open(HTML_FILE.as_uri())
    print("\nOpened in browser. To save as PDF:")
    print("  1. Press Ctrl+P (or Cmd+P on Mac)")
    print("  2. Choose 'Save as PDF' or 'Microsoft Print to PDF'")
    print("  3. Save the file")


if __name__ == "__main__":
    main()
