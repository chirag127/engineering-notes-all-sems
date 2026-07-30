# AKTU CS Notes

[![GitHub stars](https://img.shields.io/github/stars/chirag127/aktu-cs-notes?style=flat-square)](https://github.com/chirag127/aktu-cs-notes)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Live site](https://img.shields.io/badge/site-live-brightgreen?style=flat-square)](https://aktu-cs-notes.oriz.in)

AI-generated CS engineering study notes for all 8 semesters (AKTU syllabus). ChatGPT-generated markdown notes from official syllabus topics.

**Live site: https://aktu-cs-notes.oriz.in**

## Semester / Subject Index

Notes organized by semester under `allnotes/cs/`:

| Semester | Folder | Subjects |
|----------|--------|----------|
| 1st | `allnotes/cs/1/` | Engineering Physics, Chemistry, Mathematics I & II, Electrical, Electronics, Programming, Mechanical, Environment, Soft Skills + labs |
| 2nd | `allnotes/cs/2/` | Data Structures, Computer Organization, Discrete Structures, OS, Theory of Automata, Microprocessor, Python, AI |
| 3rd | `allnotes/cs/3/` | DBMS, Compiler Design, DAA, Web Designing, Computer Graphics, Machine Learning, Software Engineering, Computer Networks |
| 4th | `allnotes/cs/4/` | AI, NLP, High Performance Computing, Cryptography, Mobile Computing, IoT, Cloud Computing, Blockchain, Deep Learning |
| 5th | `allnotes/cs/5/` | Compiler Design, DBMS, DAA, Machine Learning, COI, Web Design |

Semesters 6–8 notes are generated via `scripts/` and will be added progressively.

## How Notes Were Generated

Python scripts in `scripts/` used the OpenAI API to generate detailed markdown notes for every topic in the official AKTU syllabus. Keys are read from environment variables — see `.env.example`.

```bash
cp .env.example .env
# Add your OpenAI API key to .env
pip install openai tiktoken requests
python scripts/generate_notes_threaded.py
```

| Script | Purpose |
|--------|---------|
| `generate_notes_threaded.py` | Multi-threaded generation via ChatGPT |
| `generate_notes_async.py` | Async generation via OpenAI Completions |
| `main_generator.py` | Single-key generator |
| `batch_processor.py` | Batch processing with Bing fallback |
| `bulk_input.py` | Bulk input handler |
| `post_processor.py` | Post-process and clean generated notes |
| `poe_generator.py` | POE-based generation |
| `remove_empty_notes.py` | Remove empty/stub files |
| `sem5_generate_cd_notes.py` | Sem-5 Compiler Design note generator |
| `sem5_generate_wd_notes.py` | Sem-5 Web Design note generator |
| `sem5_download_helper.py` | PDF download helper |
| `sem5_search_helper.py` | Syllabus search helper |

## Question Papers

Past AKTU exam question papers (162 PDFs) are distributed as a downloadable archive in [**Releases**](https://github.com/chirag127/aktu-cs-notes/releases) to keep this repo lightweight.

Download `aktu-question-papers.zip` from the [latest release](https://github.com/chirag127/aktu-cs-notes/releases/latest) and extract into `question-papers/`.

| Source | Subfolder | Contents |
|--------|-----------|----------|
| ABES | `abes/` | Papers from ABES Engineering College — MP, TAFL, Mathematics |
| AKTU Online | `aktuonline/` | Papers from aktuonline.com — OS, TAFL, UH subjects |
| Archive | `archive/` | Archived 3rd-semester papers (COA, DS, DSTL, CSS, TC, SI) |

Scrapers: `scripts/qp_abes.py`, `scripts/qp_aktuonline.py`, `scripts/qp_function.py`.

## Contributing

See [CONTRIBUTING.md](.github/../contributing) or open an issue using the bug-report template.

## License

MIT — see [LICENSE](LICENSE).
