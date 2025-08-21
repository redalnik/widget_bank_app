from typing import Generator
from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: "str") -> Iterator[dict]:
    """Функция принимает список словарей, представляющих транзакции и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Функция-генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """Функция-генератор, которая выдает номера банковских карт в формате "XXXX XXXX XXXX XXXX" """
    for num in range(start, stop + 1):
        str_number = str(num).zfill(16)
        yield f"{str_number[:4]} {str_number[4:8]} {str_number[8:12]} {str_number[12:16]}"
