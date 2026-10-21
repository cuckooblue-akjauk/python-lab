from python_lab.experiment_utils import save_json


def test_save_json(tmp_path):
    data = {"status": "ok", "value": 123}
    target = tmp_path / "result.json"

    save_json(data, target)

    assert target.exists()
    assert target.read_text(encoding="utf-8").strip().startswith("{")
