import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "user_details, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158-3007-3472-6758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("МИР 2200 2002 1234 567", "Неверный номер счета/карты"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 646864736788947795", "Неверный номер счета/карты"),
        ("Счет 6468647367889477958900", "Неверный номер счета/карты"),
    ],
)
def test_mask_account_card(user_details, expected):
    assert mask_account_card(user_details) == expected


@pytest.mark.parametrize(
    "received_date, expected",
    [
        ("2025-10-08T23:59:59.999999", "08.10.2025"),
        ("2025-11-06", "06.11.2025"),
        ("2025-03-10T02:26:18+03:00", "10.03.2025"),
        ("", "Некорректный формат даты")
    ],
)
def test_get_date(received_date, expected):
    assert get_date(received_date) == expected
