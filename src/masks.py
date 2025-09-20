import logging

logger = logging.getLogger(__name__)  # логгер будет с именем модуля
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера в формате
    XXXX XX** **** XXXX"""
    logger.info("Запуск функции get_mask_card_number")
    clear_card_number = "".join([number for number in card_number if number.isdigit()])
    if len(clear_card_number) == 16:
        mask_card_number = f"{clear_card_number[:4]} {clear_card_number[4:6]}{'** ****'} {clear_card_number[12:]}"
        logger.info("Успешная маскировка номера карты")
        return mask_card_number
    logger.error(f"Ошибка маскировки номера карты: {card_number}")
    return "Неверный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера"""
    logger.info("Запуск функции get_mask_account")
    clean_mask_account_number = "".join([number for number in account_number if number.isdigit()])
    if len(clean_mask_account_number) == 20:
        mask_account_number = f"**{clean_mask_account_number[-4:]}"
        logger.info("Успешная маскировка номера счета")
        return mask_account_number
    logger.error(f"Ошибка маскировки номера счета: {account_number}")
    return "Неверный номер счета"
