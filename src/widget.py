import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(user_details: str) -> str:
    """Функция принимает информацию о карте или счете и возвращает строку с замаскированным номером"""
    account_number = "".join([letter for letter in user_details if letter.isdigit()])
    account_type = " ".join([word for word in user_details.split() if all(letter.isalpha() for letter in word)])
    if len(account_number) == 16:
        return f"{account_type} {get_mask_card_number(account_number)}"
    elif len(account_number) == 20:
        return f"{account_type} {get_mask_account(account_number)}"
    else:
        return "Неверный номер счета/карты"


def get_date(received_date: str) -> str:
    """Функция принимает строку с датой в формате '2024-03-11T02:26:18.671407'
    и возвращает дату в формате 'ДД.ММ.ГГГГ'"""
    try:
        date_obj = datetime.datetime.fromisoformat(received_date)
        return date_obj.strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        return "Некорректный формат даты"
