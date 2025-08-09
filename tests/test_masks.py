import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567891234567", "1234 56** **** 4567"),
        ("1234 5678 9123 4567", "1234 56** **** 4567"),
        ("1234-5678-9123-4567", "1234 56** **** 4567"),
        ("1234 5678 9123 4567 89", "Неверный номер карты"),
        ("1234 5678 9123 45", "Неверный номер карты"),
        ("", "Неверный номер карты"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("7365-4108-4301-3587-4305", "**4305"),
        ("7365 4108 4301 35 87 43 05", "**4305"),
        ("736541084301358743", "Неверный номер счета"),
        ("7365410843013587430509", "Неверный номер счета"),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
