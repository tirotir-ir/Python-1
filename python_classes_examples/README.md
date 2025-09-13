# Python Classes — Step‑by‑Step Examples (Beginner Friendly)

This bundle shows **why** and **how** to use classes in Python, starting
from simple scripts to a tiny school system. Files are numbered so you can follow along.

## What's inside

- `01_without_classes_cars.py` — A messy approach (no classes) to model cars.
- `02_with_classes_car.py` — Clean approach using a `Car` class (factory analogy).
- `03_bank_account.py` — Real‑world example with a `BankAccount` class.
- `04_school_system/` — A mini project split into multiple files:
  - `student.py`, `teacher.py`, `course.py`, `exam.py`, `grade.py` — class definitions
  - `main.py` — demo runner
  - `uml.txt` — simple UML‑style diagram (text)
  - `__init__.py` — marks the folder as a package
- `run_all.sh` (Linux/macOS) and `run_all.bat` (Windows) — quick run helpers.

## How to run

### Option A — Run files individually
```bash
# Example
python 02_with_classes_car.py
python 03_bank_account.py

# Run the school system demo
python 04_school_system/main.py
```

### Option B — Run everything (Windows)
Double‑click `run_all.bat` or run:
```bat
run_all.bat
```

### Option C — Run everything (Linux/macOS)
```bash
chmod +x run_all.sh
./run_all.sh
```

## Learning goals (7th‑grade friendly)
- Understand **class** as a blueprint (like a factory).
- Create **objects** with attributes (data) and methods (actions).
- See how classes make code **organized**, **reusable**, and **scalable**.
- Read a simple **UML** diagram to understand relationships between classes.