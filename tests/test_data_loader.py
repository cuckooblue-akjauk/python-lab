from python_lab.data_loader import data_path, load_csv, load_json


def test_load_csv_reads_iris_rows():
    rows = load_csv(data_path("iris.csv"))
    assert len(rows) >= 10
    assert rows[0]["species"] == "setosa"


def test_load_json_reads_sample_data():
    payload = load_json(data_path("sample_input.json"))
    assert payload["name"] == "python-lab"
    assert len(payload["examples"]) == 3
