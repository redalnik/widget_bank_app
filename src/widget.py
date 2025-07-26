from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(user_details: str) -> str:
    """Функция принимает информацию о карте или счете и возвращает строку с замаскированным номером"""
    account_number = ""
    account_type = ""
    for i in user_details:
        if i.isdigit():
            account_number += i
        else:
            account_type += i
    if len(account_number) == 16:
        return f"{account_type}{get_mask_card_number(account_number)}"
    else:
        return f"{account_type}{get_mask_account(account_number)}"


# if __name__ == "__main__":
#     q = mask_account_card("Счет 73654108430135874305")
#     print(q)


def get_date(received_date: str) -> str:
    """Функция получает строку с датой и приводит ее к формату: "ДД.ММ.ГГГГ" """
    format_date = f"{received_date[8:10]}.{received_date[5:7]}.{received_date[:4]}"
    return format_date


# if __name__ == "__main__":
#     time = get_date("2024-03-11T02:26:18.671407")
#     print(time)
