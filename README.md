# Students Program

A self-contained **Python + basic HTML** student management app. Manage students and courses, record grades, generate result pages, and visualize simple stats. The repo is designed to **run locally without any external services** and also supports a **fully offline (airplane-mode) Docker** workflow.

---

## Project Description

The Students Program lets you:

- **Manage Students:** add, edit, remove, and list students (code, name, birthdate).
- **Manage Courses:** add, edit, remove, and list courses (code, name, max degree, credit hours).
- **Supply Grades:** enter grades per course and view grades for a course.
- **Generate Results:** produce per-student HTML result pages and compute simple GPA.
- **Statistics:** generate bar/pie charts from local data (matplotlib, headless).

> The repo ships with example JSON/CSV data and a **non-interactive demo mode** (`--demo`) that writes a summary HTML and a chart for quick verification.

---

## Features

### Manage Students
- Add/edit/remove students.
- View tabular listing.

### Manage Courses
- Add/edit/remove courses.
- View course catalog.

### Supply Grades
- Enter grades per course (CSV-backed).
- Display student grades for a selected course.

### Generate Results
- Produce `"<student-code>.html"` pages.
- GPA calculation using course max degree / credit hours.

### Statistics
- **Bar chart:** registrations per course.
- **Pie chart:** course registration distribution.

---

## Tech & Requirements

- **Local (dev):** Python ≥ 3.8 (3.11 recommended)
- **Charts:** `matplotlib` (repo includes pinned wheels for Docker)
- **Container:** Docker Engine / Docker Desktop
- **OS:** Windows/macOS/Linux (examples below show Windows cmd; macOS/Linux equivalents included)

---

## Repository Layout

```

.
├─ main.py                 # Entry point (interactive menu + --demo)
├─ students.py             # Students CRUD + JSON I/O
├─ courses.py              # Courses CRUD + JSON I/O
├─ grades.py               # Grade entry / CSV helpers
├─ results.py              # Results, GPA helpers, HTML generation
├─ statics.py              # Chart/plot helpers (matplotlib)
├─ students.json           # Example student records
├─ courses.json            # Example course records
├─ cs.csv                  # Example grades (course "cs")
├─ math2.csv               # Example grades (course "math2")
├─ Dockerfile.offline      # Offline build (installs from ./wheels only)
├─ wheels/                 # Vendored manylinux wheels for Python 3.11
└─ README.md

````

---

## Data Formats

### `students.json`
```json
[
  { "code": "S001", "name": "Alice", "birthdate": "2002-05-01" },
  { "code": "S002", "name": "Bob",   "birthdate": "2001-11-12" }
]
````

### `courses.json`

```json
[
  { "code": "cs",    "name": "Computer Science", "max_degree": 100, "credit_hours": 3 },
  { "code": "math2", "name": "Math II",          "max_degree": 100, "credit_hours": 4 }
]
```

### `<course-code>.csv`

CSV per course. The app is tolerant: a header row is optional; it reads the first two columns as `(student_code, grade)` if headers don’t match common names.

```csv
student_code,grade
S001,86
S002,91
```

---

## Quickstart (Demo, non-interactive)

This is the fastest way to verify everything works. It produces:

* `out/index.html`
* `out/registrations_per_course.png`

### Windows (cmd)

```bat
python -m venv .venv
.\.venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt
python main.py --demo --out out
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
python main.py --demo --out out
```

**Expected end state**

```
out/
  index.html
  registrations_per_course.png
```

---

## Full Interactive Usage

Run without `--demo` to use the menu:

```bat
.\.venv\Scripts\python.exe main.py
```

Menu:

```
(1) Add/Edit/Remove students information
(2) Courses information
(3) Supply / view grades to students per course
(4) Final result
(5) Pie (statistics)
(6) Exit
```

* **(1)** Students: add/edit/remove/list
* **(2)** Courses: add/edit/remove/list
* **(3)** Grades: supply grades (writes CSV) / display grades for a course
* **(4)** Final result: generate per-student HTML (e.g., `S001.html`)
* **(5)** Statistics: bar/pie or both
* **(6)** Exit

---

## Offline Docker (Airplane Mode)

This repo includes `wheels/` (vendored manylinux wheels for Python **3.11**) and `Dockerfile.offline`. Build/run **with networking disabled**.

> First time only: you may need to pre-pull the base image while online:
> `docker pull python:3.11-slim`

### Build (no internet)

```bat
docker build --network=none -t sms-offline -f Dockerfile.offline .
```

### Run (no network) and write artifacts to `out/`

**Windows cmd** (adjust path as needed):

```bat
docker run --rm --network=none ^
  -v "%CD%\out:/out" ^
  sms-offline python main.py --demo --out /out
```

**macOS/Linux**

```bash
docker run --rm --network=none \
  -v "$PWD/out:/out" \
  sms-offline python main.py --demo --out /out
```

**Expected end state**

```
out/
  index.html
  registrations_per_course.png
```

---

## CLI Reference

```text
--demo              Generate summary HTML and chart non-interactively.
--out <dir>         Output directory for demo artifacts (default: ./out).
(no flags)          Launch interactive menu in terminal.
```

> Notes:
>
> * `main.py` configures matplotlib’s headless backend automatically in demo mode, so Docker runs without a display (no X/GUI needed).
> * The demo reads **existing** `students.json`, `courses.json`, and all `*.csv` in the repo root.

---

## Troubleshooting

**Q: Docker build tries to access the internet.**
A: Ensure `Dockerfile.offline` is used and `wheels/` contains manylinux wheels for **all** packages pinned in `requirements.txt`. If you add a package, regenerate wheels:

```bash
# Build wheels for Python 3.11 inside a temp container (online once)
docker run --rm -v "$PWD:/app" python:3.11-slim bash -lc \
  "python -m pip install -U pip wheel && python -m pip wheel -r /app/requirements.txt -w /app/wheels"
```

**Q: ImportError for matplotlib in container.**
A: A wheel may be missing or versions don’t match. Keep `requirements.txt` exactly in sync with `wheels/` contents.

**Q: Demo produced no files.**
A: Check that `students.json`, `courses.json`, and at least one `<course>.csv` exist. The demo counts rows and will still write `index.html` even if counts are zero.

**Q: Windows path mount fails.**
A: Use absolute paths and quotes, e.g.
`-v "C:\full\path\to\repo\out:/out"`.

---

## Development Tips

* Create a feature branch (e.g., `devops/offline`, `feat/xyz`), commit often, and open a PR.
* Keep `requirements.txt` minimal and **pinned**.
* If you modify plotting, prefer non-interactive backends (e.g., `Agg`) for portability.
* Add new sample data under version control for deterministic demos.

---

## Contributing

1. Create a branch: `git switch -c feat/your-change`
2. Run local demo: `python main.py --demo --out out`
3. Add/adjust tests or demo data if needed.
4. Open a PR; include a copy-paste “How to verify” section:

   ```bash
   docker build --network=none -t sms-offline -f Dockerfile.offline .
   docker run --rm --network=none -v "$PWD/out:/out" sms-offline python main.py --demo --out /out
   ```

---

## License
all rights reserved