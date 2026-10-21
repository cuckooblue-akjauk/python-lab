from pathlib import Path
import importlib.util
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

EXPERIMENTS = ROOT / "experiments"


def list_experiments() -> list[str]:
    names = []
    for path in sorted(EXPERIMENTS.glob("*.py")):
        if path.name.startswith("_"):
            continue
        if path.name == "__init__.py":
            continue
        names.append(path.name)
    return names


def load_module(script_path: Path):
    spec = importlib.util.spec_from_file_location(script_path.stem, script_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load module from {script_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[script_path.stem] = module
    spec.loader.exec_module(module)
    return module


def run_experiment(name: str):
    script_path = EXPERIMENTS / name
    if not script_path.exists():
        raise FileNotFoundError(f"Experiment not found: {name}")

    module = load_module(script_path)
    if hasattr(module, "main"):
        return module.main()
    raise AttributeError(f"{name} does not define a main() function")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        experiments = list_experiments()
        print("Available experiments:")
        for item in experiments:
            print(f"- {item}")
        sys.exit(0)

    run_experiment(sys.argv[1])
