from run_experiments import list_experiments, run_experiment


def test_list_experiments_contains_known_scripts():
    names = list_experiments()
    assert "001_basic_example.py" in names
    assert "template_experiment.py" in names


def test_run_experiment_executes_basic_example():
    result = run_experiment("001_basic_example.py")
    assert result is None
