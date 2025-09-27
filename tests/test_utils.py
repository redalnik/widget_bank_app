from unittest.mock import mock_open
from unittest.mock import patch

from src.utils import load_transactions
from src.utils import process_bank_operations
from src.utils import process_bank_search


def test_load_transaction_not_a_list(sample_dict_in_utils):
    result = load_transactions(sample_dict_in_utils)
    assert result == []


def test_load_transactions_with_fix_json(sample_fake_jason_in_utils):
    with patch("builtins.open", mock_open(read_data=sample_fake_jason_in_utils)) as js:
        result = load_transactions("any_json_file.json")
    assert result == [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26"}]
    js.assert_called_once_with("any_json_file.json", "r", encoding="utf-8")  # вызвана 1 раз


def test_load_transaction_with_mock_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_transactions("json.json")
    assert result == []


def test_load_transactions_invalid_json(capsys):
    fake_json = "{broken json}"
    with patch("builtins.open", mock_open(read_data=fake_json)):
        result = load_transactions("fake_path.json")
    captured = capsys.readouterr()
    assert result == []
    assert "Произошла ошибка при чтении файла" in captured.out


@patch("builtins.open", side_effect=FileNotFoundError)
def test_load_transactions_file_not_found(mock_file, capsys):
    result = load_transactions("nofile.json")
    assert result == []
    captured = capsys.readouterr()
    assert "Файл nofile.json не найден" in captured.out


def test_process_bank_search(csv_excel_file_return):
    result = process_bank_search(csv_excel_file_return, "перевод")
    assert len(result) == 2


def test_transactions_with_invalid_description(csv_excel_file_return):
    result = process_bank_search(csv_excel_file_return, "услуг")
    assert len(result) == 1


def test_transactions_with_empty_search(csv_excel_file_return):
    result = process_bank_search(csv_excel_file_return, "")
    assert len(result) == 3


def test_invalid_categories_type():
    transactions = [{'description': 'Перевод организации'}]
    result = process_bank_operations(transactions, "перевод")
    assert result == {}


def test_empty_categories_list(csv_excel_file_return):
    result = process_bank_operations(csv_excel_file_return, [])
    assert result == {}
