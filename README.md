# Engineering Notes — All Semesters

[![GitHub stars](https://img.shields.io/github/stars/chirag127/engineering-notes-all-sems?style=flat-square)](https://github.com/chirag127/engineering-notes-all-sems)
[![License](https://img.shields.io/github/license/chirag127/engineering-notes-all-sems?style=flat-square)](LICENSE)
[![GH Pages](https://img.shields.io/badge/site-live-brightgreen?style=flat-square)](https://chirag127.github.io/engineering-notes-all-sems/)

AI-generated study notes for Computer Science engineering (AKTU). Generated using ChatGPT from official AKTU syllabus topics.

## Live Site

**https://chirag127.github.io/engineering-notes-all-sems/**

## Contents

Notes organized by semester under `allnotes/cs/`:

| Semester | Folder | Subjects |
|----------|--------|----------|
| 1st | `allnotes/cs/1/` | Engineering Physics, Chemistry, Mathematics, Electrical, Electronics, Programming, Mechanical, Environment, Soft Skills + labs |
| 2nd | `allnotes/cs/2/` | Data Structures, Computer Organization, Python, AI, and more |
| 3rd | `allnotes/cs/3/` | DBMS, Compiler Design, Human Computer Interface, and more |
| 4th | `allnotes/cs/4/` | AI, Mobile Computing, IoT, Cloud Computing, Blockchain, and more |

Each subject has one `.md` file with detailed AI-generated explanations covering all syllabus topics.

## Note Generator Scripts

`scripts/` contains Python scripts that generated these notes using the OpenAI API.

```bash
cp .env.example .env
# Add your OpenAI API keys to .env
pip install revChatGPT openai tiktoken requests
python scripts/generate_notes_threaded.py
```

| Script | Purpose |
|--------|---------|
| `generate_notes_threaded.py` | Multi-threaded note generation via ChatGPT |
| `generate_notes_async.py` | Async note generation via OpenAI Completions API |
| `main_generator.py` | Single-key note generator |
| `batch_processor.py` | Batch processing with Bing fallback |
| `bulk_input.py` | Bulk input handler |
| `post_processor.py` | Post-process and clean generated notes |
| `poe_generator.py` | POE-based note generation |
| `remove_empty_notes.py` | Remove empty/stub note files |

## License

MIT
