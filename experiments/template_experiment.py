from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from python_lab.experiment_utils import print_banner, save_json


def run_experiment() -> dict:
    print_banner("Template Experiment")
    result = {
        "status": "ok",
        "idea": "Example experiment result",
        "value": 42,
    }
    print(result)
    return result


def main():
    result = run_experiment()
    output_dir = ROOT / "artifacts"
    save_json(result, output_dir / "template_experiment.json")


if __name__ == "__main__":
    main()
