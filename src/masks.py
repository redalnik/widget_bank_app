def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера в формате
    XXXX XX** **** XXXX"""
    mask_card_number = f"{card_number[:6]}{'*' * 6}{card_number[-4:]}"
    split_number = []
    for i in range(0, len(mask_card_number), 4):
        split_number.append(mask_card_number[i : i + 4])
    return " ".join(split_number)


# if __name__ == "__main__":
#     print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера"""
    mask_account_number = f"**{account_number[-4:]}"
    return mask_account_number


# if __name__ == "__main__":
#     print(get_mask_account("73654108430135874305"))
