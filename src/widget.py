from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(user_details: str) -> str:
    """Функция принимает информацию о карте или счете и выводит строку с замаскированным номером"""
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
