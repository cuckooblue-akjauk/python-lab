from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from python_lab.experiment_utils import print_banner


def run_example():
    print_banner("Basic Example")
    sample_data = ["alpha", "beta", "gamma"]
    for item in sample_data:
        print(f"Processing: {item}")


def main():
    run_example()


if __name__ == "__main__":
    main()
