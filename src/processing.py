def filter_by_state(bank_operation: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей по значению ключа 'state'"""
    return [operation for operation in bank_operation if operation.get("state") == state]
