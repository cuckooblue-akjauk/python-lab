from pathlib import Path
import csv
import json


def load_csv(path: str | Path):
    file_path = Path(path)
    with file_path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def load_json(path: str | Path):
    file_path = Path(path)
    with file_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def data_path(*parts: str) -> Path:
    root = Path(__file__).resolve().parents[2]
    return root.joinpath("data", *parts)
