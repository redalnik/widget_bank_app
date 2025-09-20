import json
import logging
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
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Данные успешно загружены")
                return data
            else:
                logger.warning(f"Некорректный тип данных: {type(data)}")
                return []
    except FileNotFoundError:
        logging.error(f"Ошибка, файл {file_path} не найден ")
        print(f"Файл {file_path} не найден")
        return []
    except Exception as e:
        logging.error(f"Непредвиденная ошибка: {e}.")
        print(f"Произошла ошибка при чтении файла: {e}.")
        return []
