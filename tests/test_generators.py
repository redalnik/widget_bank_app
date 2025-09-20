import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


def test_filter_by_usd_currency(filter_usd_transactions, all_transactions):
    """Обработка по поиску USD"""
    result = list(filter_by_currency(all_transactions, "USD", ))
    assert result == filter_usd_transactions


@pytest.mark.parametrize("currency,expected_ids", [
    ("USD", [939719570, 142264268, 895315941]),
    ("RUB", [873106923, 594226727]),
    ("EUR", []),
    ("GBP", []),
])
def test_currency_filter(all_transactions, currency, expected_ids):
    """Тестирование фильтрации по разным валютам"""
    result = list(filter_by_currency(all_transactions, currency))
    assert [t["id"] for t in result] == expected_ids


def test_filter_by_not_currency(all_transactions):
    """Обработка, когда нет искомой валюты"""
    result = list(filter_by_currency(all_transactions, "EUR", ))
    assert result == []


def test_empty_transactions():
    """Обработка пустого списка"""
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions(all_transactions, all_description):
    """Возвращает описание всех операций"""
    result = list(transaction_descriptions(all_transactions))
    assert result == all_description


def test_transaction_descriptions_empty():
    """Тест на пустой список"""
    result = list(transaction_descriptions([]))
    assert result == []


def test_card_number_generator(card_number_generated):
    """Тест генератора номеров"""
    result = list(card_number_generator(1, 5))
    assert result == card_number_generated
