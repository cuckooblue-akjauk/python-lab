from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from python_lab.experiment_utils import print_banner, save_json


def prompt_experiment(prompt: str) -> dict:
    response = {
        "prompt": prompt,
        "result": "This is a placeholder result for testing prompt behavior.",
        "tokens_estimate": len(prompt.split()),
    }
    return response


def main():
    print_banner("Prompt Experiment")
    prompt = "What are the main tradeoffs of using Python for rapid prototyping?"
    result = prompt_experiment(prompt)
    print(result)

    output_path = ROOT / "artifacts" / "prompt_experiment.json"
    save_json(result, output_path)


if __name__ == "__main__":
    main()
