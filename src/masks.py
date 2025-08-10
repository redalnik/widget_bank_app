def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера в формате
    XXXX XX** **** XXXX"""
    clear_card_number = "".join([number for number in card_number if number.isdigit()])
    if len(clear_card_number) == 16:
        mask_card_number = f"{clear_card_number[:4]} {clear_card_number[4:6]}{'** ****'} {clear_card_number[12:]}"
        return mask_card_number
    return "Неверный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера"""
    clean_mask_account_number = "".join([number for number in account_number if number.isdigit()])
    if len(clean_mask_account_number) == 20:
        mask_account_number = f"**{clean_mask_account_number[-4:]}"
        return mask_account_number
    return "Неверный номер счета"
