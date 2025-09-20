import json
from typing import Any
from typing import Dict
from typing import List


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает данные о финансовых транзакциях из JSON-файла."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []


# if __name__ == "__main__":
#     transactions = load_transactions("../data/operations.json")
#     print(transactions)
