import json
import logging
import re
from collections import Counter
from typing import Any
from typing import Dict
from typing import List

logger = logging.getLogger(__name__)  # логгер будет с именем модуля
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает данные о финансовых транзакциях из JSON-файла."""
    logger.info("Запуск функции load_transactions")
    try:
        logger.info(f"Попытка чтения файла {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Данные успешно загружены")
                return data
            else:
                logger.warning(f"Некорректный тип данных: {type(data)}")
                return []
    except FileNotFoundError:
        logger.error(f"Ошибка, файл {file_path} не найден ")
        print(f"Файл {file_path} не найден")
        return []
    except Exception as e:
        logger.error(f"Непредвиденная ошибка: {e}.")
        print(f"Произошла ошибка при чтении файла: {e}.")
        return []


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Фильтрует список банковских операций по наличию строки поиска в описании."""
    pattern = re.compile(search, re.IGNORECASE)
    result = []
    for transaction in data:
        description = transaction.get("description")
        if isinstance(description, str) and pattern.search(description):
            result.append(transaction)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Считает количество банковских операций по заданным категориям."""
    if isinstance(categories, str):
        return {}
    logger.info("Запуск функции process_bank_operations")
    categories = [category.lower() for category in categories]
    counter: Counter = Counter()
    for transaction in data:
        description = transaction.get("description")
        if not isinstance(description, str):
            continue
        description_lower = description.lower()
        for category in categories:
            if category in description_lower:
                counter[category] += 1
    logger.info(f"Результат подсчёта: {counter}")
    return dict(counter)
