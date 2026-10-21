# Python Lab

A lightweight sandbox for trying out new Python techniques, mini experiments, and quick data explorations.

## Purpose

This repo is intentionally simple:
- `experiments/` holds one-off ideas and scripts
- `src/python_lab/` holds reusable helpers
- `data/` contains example datasets for experiments
- `tests/` verifies useful logic

## Quick start

```bash
cd python-lab
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run experiments

List all experiments:

```bash
python run_experiments.py
```

Run a single experiment:

```bash
python run_experiments.py 001_basic_example.py
python run_experiments.py 002_prompt_experiment.py
python run_experiments.py template_experiment.py
```

## Run tests

```bash
pytest
```

## Datasets

The repo includes a few common starter datasets:

- `data/iris.csv` - classic machine learning dataset with flower measurements
- `data/titanic.csv` - common classification example
- `data/sample_input.json` - small JSON example for quick experiments

## Typical workflow

1. Try a new idea in `experiments/`
2. If it becomes useful, move logic into `src/python_lab/`
3. Add a test in `tests/`
4. Save outputs under `artifacts/`

## Environment variables

Copy `.env.example` to `.env` if you want to use environment-based config:

```bash
cp .env.example .env
```

## Recommended structure for a new experiment

```python
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from python_lab.experiment_utils import print_banner, save_json


def run_experiment():
    print_banner("My Experiment")
    result = {"status": "ok", "value": 1}
    print(result)
    return result


def main():
    result = run_experiment()
    save_json(result, ROOT / "artifacts" / "my_experiment.json")


if __name__ == "__main__":
    main()
```
