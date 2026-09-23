import pandas as pd

TARGET = "Selector"
REQUIRED = {TARGET, "Gender"}

def load_data():
    column_names = [
        "Age", "Gender", "TB", "DB", "Alkphos", "Sgpt", "Sgot",
        "TP", "ALB", "AG_Ratio", "Selector"
    ]
    return pd.read_csv("data/raw/dataset.csv", header=None, names=column_names)

def test_dataset_is_not_empty():
    assert not load_data().empty

def test_required_columns_exist():
    assert REQUIRED <= set(load_data().columns)

def test_target_has_no_missing_and_two_classes():
    y = load_data()[TARGET]
    assert y.notna().all()
    assert y.nunique() >= 2