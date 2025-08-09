def filter_by_state(bank_operation: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей по значению ключа 'state'"""
    return [operation for operation in bank_operation if operation.get("state") == state]


def sort_by_date(bank_operation: list[dict], decreasing: bool = True) -> list[dict]:
    """Функция возвращает новый список, отсортированный по дате, (по умолчанию — убывание)."""
    return sorted(bank_operation, key=lambda x: x.get("date"), reverse=decreasing)


# if __name__ == "__main__":
#     filter_list = filter_by_state(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
#     print(filter_list)

# if __name__ == "__main__":
#     date_list = sort_by_date(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ], False
#     )
#     print(date_list)
