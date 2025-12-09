# Enginuity Portfolio: Python Engineering Coursework Archive

> This repository is a professionally archived collection of advanced Python scripts and academic projects developed during intensive 4th-year engineering studies. It serves as a static, high-fidelity historical snapshot of foundational data structures, algorithmic design, and simulation coursework.

## 🛡️ Project Integrity & Status

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/chirag127/EnginuityPortfolio-Python-Engineering-Coursework-Archive/ci.yml?branch=main&style=flat-square&label=CI%2FCD)](https://github.com/chirag127/EnginuityPortfolio-Python-Engineering-Coursework-Archive/actions/workflows/ci.yml)
[![Project Status](https://img.shields.io/badge/Status-Retired%20Product-990000?style=flat-square)](https://github.com/chirag127/EnginuityPortfolio-Python-Engineering-Coursework-Archive/blob/main/.github/SECURITY.md)
[![Code Language](https://img.shields.io/badge/Language-Python%203.10%2B-blue?style=flat-square)](https://www.python.org/)
[![Linting & Formatting](https://img.shields.io/badge/Code%20Quality-Ruff-6633cc?style=flat-square)](https://github.com/astral-sh/ruff)
[![License](https://img.shields.io/github/license/chirag127/EnginuityPortfolio-Python-Engineering-Coursework-Archive?style=flat-square&color=orange)](https://github.com/chirag127/EnginuityPortfolio-Python-Engineering-Coursework-Archive/blob/main/LICENSE)

[![GitHub Stars](https://img.shields.io/github/stars/chirag127/EnginuityPortfolio-Python-Engineering-Coursework-Archive?style=social)](https://github.com/chirag127/EnginuityPortfolio-Python-Engineering-Coursework-Archive)

---

## 📝 Table of Contents

1.  [Overview & Purpose](#-overview--purpose)
2.  [Repository Architecture](#-repository-architecture)
3.  [AI Agent Directives (CRITICAL)](#-ai-agent-directives-critical)
4.  [Local Setup & Execution](#-local-setup--execution)
5.  [Key Coursework Modules](#-key-coursework-modules)
6.  [License & Copyright](#-license--copyright)

---

## 💡 Overview & Purpose

This archive captures the technical proficiency gained through rigorous computer science and engineering modules. It is designed not for ongoing development but as a showcase of fundamental Python expertise applied to complex problems, demonstrating competency in efficiency, data handling, and standard library utilization.

While this product is retired, the underlying academic principles and code structure adhere to high professional standards.

## 📂 Repository Architecture

The structure follows a clean, module-centric layout, isolating assignments and data for clarity. Each top-level directory corresponds to a major engineering course or focus area.

text
EnginuityPortfolio/
├── algorithms_and_ds/
│   ├── search_routines.py
│   ├── sorting_benchmarks.py
│   └── README.md
├── simulation_and_modeling/
│   ├── ode_solver.py
│   └── visualization_scripts.py
├── data_analysis_tools/
│   ├── pandas_cleaner.py
│   └── data/
├── tests/
│   ├── test_search_routines.py
│   └── test_ode_solver.py
├── .github/
├── pyproject.toml
└── README.md


## 🤖 AI Agent Directives (CRITICAL)

<details>
<summary><strong>📐 APEX Architectural Mandates & Toolchain Specifications (Target 2026 Standard)</strong></summary>

### 1. IDENTITY & CONTEXT

**Role:** Senior Principal Software Architect (Apex Technical Authority).
**Context:** This repository is a historical artifact. All maintenance tasks (linting, testing) are designed to validate the historical integrity of the code structure.

### 2. CORE APEX TECH STACK (Python)

| Component | Tool / Framework | Purpose | Directive |
| :--- | :--- | :--- | :--- |
| **Package Manager** | `uv` | Ultra-fast dependency resolution and environment management. | Use `uv sync` to manage virtual environments. | 
| **Linter/Formatter** | `Ruff` | Unified, highly performant Python code quality enforcement. | Zero tolerance for linting errors (`ruff check`). | 
| **Testing Framework** | `Pytest` | Robust unit and integration testing engine. | Achieve high test coverage in `tests/`. | 

### 3. ARCHITECTURAL PRINCIPLES

*   **Modular Monolith:** Code within each coursework module (`algorithms_and_ds/`, etc.) must be self-contained and expose clear, minimal interfaces.
*   **Readability Over Novelty (RON):** Since this is an archive, code must be maximally readable for educational review. Use clear, descriptive variable names (`snake_case` mandatory).
*   **Type Hinting:** All functions and methods must utilize modern Python type hints (`Python 3.10+` standards).

### 4. VERIFICATION COMMANDS

Future automated agents must execute these commands to ensure code integrity upon cloning:

bash
# 1. Environment Setup (using uv, ensuring Python 3.10+)
uv venv
source .venv/bin/activate
uv sync

# 2. Code Quality Check (Linter/Formatter)
ruff check .
ruff format --check .

# 3. Execute Tests
pytest


</details>

---

## 🚀 Local Setup & Execution

To explore or run the archived scripts locally, follow these steps. The code requires Python 3.10+.

### Prerequisites

Ensure you have `git` and `uv` (the fast Python package manager) installed.

### Installation Steps

bash
# 1. Clone the repository
git clone https://github.com/chirag127/EnginuityPortfolio-Python-Engineering-Coursework-Archive.git
cd EnginuityPortfolio-Python-Engineering-Coursework-Archive

# 2. Create and activate virtual environment using uv
uv venv
source .venv/bin/activate

# 3. Install dependencies
uv sync

# 4. Run verification tests (Optional, but recommended)
pytest


### Running Specific Scripts

Navigate into a module directory and execute the script directly:

bash
# Example: Running an algorithm script
python algorithms_and_ds/search_routines.py


## 📚 Key Coursework Modules

| Module Directory | Primary Focus Area | Description |
| :--- | :--- | :--- |
| `algorithms_and_ds/` | Computer Science Fundamentals | Implementations of complex data structures, graph algorithms, and efficiency analysis (Big O). |
| `simulation_and_modeling/` | Mathematical Engineering | Scripts for numerical methods, differential equations (ODEs), and system behavior simulations. |
| `data_analysis_tools/` | Data Engineering & Cleansing | Projects focusing on data manipulation, ETL processes, and utilizing libraries like Pandas and NumPy for complex analysis. |

## ⚖️ License & Copyright

This archived work is protected under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) License**.

**You are free to:**
*   **Share** — copy and redistribute the material in any medium or format.
*   **Adapt** — remix, transform, and build upon the material.

**Under the following terms:**
*   **Attribution:** You must give appropriate credit, provide a link to the license, and indicate if changes were made.
*   **Non-Commercial:** You may not use the material for commercial purposes.