import pytest
from clean_data import clean_rows

def test_good_row():
    row = {"id": "1", "provider": "Provider A", "status": "completed", "minutes": "30"}
    result = clean_rows(row)
    assert result["minutes"] == 30

def test_missing_provider():
    row = {"id": "4", "provider": "", "status": "completed", "minutes": "45"}
    with pytest.raises(ValueError):
        clean_rows(row)