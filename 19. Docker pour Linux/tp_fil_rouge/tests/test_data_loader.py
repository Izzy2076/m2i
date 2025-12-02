import pytest
import pandas as pd
from src import data_loader


def test_load_csv_success():
    csv_file = "./data/raw/dirty_cafe_sales.csv"

    result = data_loader.load_csv(str(csv_file))

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 10000
    assert 'Item' in result.columns


def test_load_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        data_loader.load_csv('test.csv')


def test_load_csv_empty_file(tmp_path):
    csv_file = "./data/data_test/empty.csv"

    with pytest.raises(ValueError):
        data_loader.load_csv(str(csv_file))