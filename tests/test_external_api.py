from unittest.mock import patch

from src.external_api import transaction_amount  # путь поправь под свой проект


def test_transaction_amount_rub(sample_dict_in_utils):
    transaction = sample_dict_in_utils
    assert transaction_amount(transaction) == 31957.58


def test_transaction_amount_invalid():
    wrong_transaction = {"wrong": "data"}
    result = transaction_amount(wrong_transaction)
    assert result == 0.0


@patch("requests.request")
def test_transaction_amount_usd(mock_request, sample_dict_usd_transaction):
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = {"result": 8500.85}
    result = transaction_amount(sample_dict_usd_transaction)
    assert result == 8500.85
    mock_request.assert_called_once()


@patch("src.external_api.API_KEY", None)
def test_transaction_amount_no_api_key_returns_zero(sample_dict_usd_transaction):
    result = transaction_amount(sample_dict_usd_transaction)
    assert result == 0.0
