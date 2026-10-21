from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from python_lab.data_loader import data_path, load_csv
from python_lab.experiment_utils import print_banner


def run_experiment():
    print_banner("Iris Dataset Exploration")
    rows = load_csv(data_path("iris.csv"))
    print(f"Loaded {len(rows)} rows")
    print(f"Columns: {list(rows[0].keys())}")
    print(f"Sample row: {rows[0]}")


def main():
    run_experiment()


if __name__ == "__main__":
    main()
