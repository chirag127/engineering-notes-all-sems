# AI Notes Toolkit

[![GitHub stars](https://img.shields.io/github/stars/chirag127/ai-notes-toolkit?style=flat-square)](https://github.com/chirag127/ai-notes-toolkit)
[![License](https://img.shields.io/github/license/chirag127/ai-notes-toolkit?style=flat-square)](LICENSE)
[![Live Site](https://img.shields.io/badge/site-live-brightgreen?style=flat-square)](https://chirag127.github.io/ai-notes-toolkit/)
[![Python](https://img.shields.io/badge/python-3.10+-blue?style=flat-square)](https://python.org)

Python scripts for generating AI-powered study notes using Bing and POE APIs. Includes generated CS engineering notes in markdown format.

## Live Site

**https://chirag127.github.io/ai-notes-toolkit/**

## Scripts

| Script | Description |
|--------|-------------|
| `scripts/01_bing_generator.py` | Generate notes via Bing AI |
| `scripts/02_poe_generator.py` | Generate notes via POE AI |
| `scripts/poe_client.py` | POE API client |
| `scripts/03_remove_links.py` | Strip links from generated notes |
| `scripts/05_add_odd_lines.py` | Process note files |
| `scripts/06_merge_markdowns.py` | Merge markdown files |
| `scripts/07_markdown_to_pdf.py` | Convert markdown to PDF |
| `scripts/16_pdf_ocr.py` | OCR PDF files |
| `scripts/download_question_papers.py` | Download question papers |
| `scripts/merge_markdowns_v2.py` | Alternate markdown merger |
| `scripts/merge_pdfs.py` | Merge multiple PDFs |
| `scripts/merge_pdf_single.py` | Merge single PDF set |

## Generated Notes

Notes in `notes/` and `allnotes/` organized by subject and AI model (Bing Balanced/Creative/Precise, POE capybara/chinchilla/nutria).

Subjects include Software Engineering and allied CS topics.

## Requirements

```bash
pip install requests beautifulsoup4 pdfkit markdown
```

## License

MIT
