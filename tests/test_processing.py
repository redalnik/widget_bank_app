from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state(operations_data, data_executed, data_canceled):
    assert filter_by_state(operations_data, "EXECUTED") == data_executed
    assert filter_by_state(operations_data, "CANCELED") == data_canceled


def test_sort_by_date(operations_data, date_reverse_true, date_reverse_false):
    assert sort_by_date(operations_data, True) == date_reverse_true
    assert sort_by_date(operations_data, False) == date_reverse_false
