import pytest
from fetch import fetch_data
from transform import clean_data

def test_fetch_returns_data( ):
    data = fetch_data()
    assert data is not None
    assert len(data) > 0

def test_fetch_returns_expected_columns():
    data = fetch_data()
    cleaned = clean_data(data)
    expected_columns = ['variant_id', 'variant_name', 'unit', 'date', 'price']
    for col in expected_columns:
        assert col in cleaned.columns
