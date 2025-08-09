def filter_by_state(bank_operation: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей по значению ключа 'state'"""
    return [operation for operation in bank_operation if operation.get("state") == state]


def sort_by_date(bank_operation: list[dict], decreasing: bool = True) -> list[dict]:
    """Функция возвращает новый список, отсортированный по дате, (по умолчанию — убывание)."""
    return sorted(bank_operation, key=lambda x: x["date"], reverse=decreasing)
