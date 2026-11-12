# python_auto_tools

A collection of small, focused Python automation utilities built as a
personal engineering project. Each tool is self-contained, tested,
and documented so that it can be reused, extended, or dropped into
other workflows without surprises.

---

## 1. Purpose

`python_auto_tools` is a **mono-repo of independent automation scripts**.
The goal is not to build one giant framework, but to accumulate a
toolbox of reliable, well-documented utilities that solve concrete
problems (network probing, file processing, log parsing, etc.).

Every tool in this repo must satisfy the same contract:

- Runs from a clean virtual environment with `pip install -r requirements.txt`
- Has a `README` or docstring explaining **what it does and why**
- Exits with code `0` on success and non-zero on failure
- Does not write to global state (no installs outside the venv, no
  hard-coded absolute paths)

---

## 2. Scope — What We Are Building (and How Much)

This repo is intentionally **small and finite**. The scope is:

| # | Tool | Purpose | Status |
|---|------|---------|--------|
| 1 | `test_requests.py` | Minimal HTTP client exercise: send GET/POST, print status, headers, body. Used to validate `requests` install and network reachability.
| 2 | `file_organizer.py` | Sort files in a directory into subfolders by extension or date. Dry-run by default.  
| 3 | `log_parser.py` | Parse a log file, extract lines matching a pattern, output a summary count. 
| 4 | `port_scanner.py` | Simple TCP connect scan against a host/port list (educational only, local targets). 
| 5 | `os_tests.py` | What you use after you get a shell to figure out where you are, who you are, and how to escape.

**How much?** Five tools total for v1.0. No more. Resist scope creep.
Each tool should be **under ~150 lines** and readable in one sitting.
If a tool grows beyond that, it gets its own repository.

---

## 3. Repository Layout
```text
python_auto_tools/
├── .gitignore
├── README.md
├── requirements.txt
├── src/
│ ├── test_requests.py
│ ├── file_organizer.py
│ ├── log_parser.py
│ └── port_scanner.py
| └──os_tests.py  
├── tests/
│ └── test_smoke.py
└── docs/
└── notes.md
```


- `src/` — all runnable scripts live here
- `tests/` — smoke tests (one per tool is enough for v1)
- `docs/` — longer notes, screenshots, experiment logs

---

## 4. Environment Setup

```bash
- 1. Clone
git clone <your-ssh-url> python_auto_tools
cd python_auto_tools

- 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

- 3. Install dependencies
pip install -r requirements.txt
```
Verification: your prompt must show (.venv) before you run
anything. If it doesn't, you are in the wrong environment — stop and fix it.

## 5. Running a Tool
```bash
python src/test_requests.py
```
Each script should be runnable directly from the repo root. No
package install step, no PYTHONPATH tricks.

## 6. Dependency Policy
Dependencies are pinned in requirements.txt via pip freeze.

After every pip install <pkg>, immediately run:

```bash
pip freeze > requirements.txt
```
Do not commit .venv/. It is in .gitignore for a reason.

## 7. Contribution Workflow (Even If You Are the Only Contributor)
Follow this every single time, even solo. The discipline is the point.
```bash
git status                         # 1. inspect what changed
git add .                          # 2. stage
git commit -m "feat: add port_scanner"   # 3. conventional commit message
git push                           # 4. publish
Commit message prefixes: feat:, fix:, docs:, chore:, test:, refactor:.
```
**Never commit:**

.venv/

__pycache__/

*.pyc

Zone.Identifier or other OS junk

Large binaries or screenshots over ~1 MB

## 8. Definition of Done (per tool)
A tool is not "done" until all of the following are true:

□ Script runs from a clean venv without errors
□ Exit code is 0 on success, non-zero on failure
□ Docstring at the top explains purpose, inputs, outputs
□ At least one smoke test in tests/
□ requirements.txt is up to date
□ Committed with a conventional message and pushed
□ One paragraph in docs/notes.md describing what was learned

## 9. Roadmap
v0.1 — test_requests.py working and pushed

v0.2 — file_automation.py 

v0.3 — log_parser.py

v0.4 — port_scanner.py (local targets only)

v0.5 _ os_tests.py

v1.0 — all five tools done, tests passing, README final

Anything after v1.0 is a new project, not a new folder in this repo.

## 10. License
Personal project. MIT-style — use at your own risk, no warranty.