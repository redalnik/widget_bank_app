from src.csv_excel_reader import read_csv_file
from src.csv_excel_reader import read_excel_file
from src.generators import filter_by_currency
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.utils import load_transactions
from src.utils import process_bank_search
from src.widget import get_date
from src.widget import get_operation_amount
from src.widget import mask_account_card


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_choice = input().strip()

    if file_choice == "1":
        print("Для обработки выбран JSON-файл.")
        data = load_transactions("data/operations.json")
    elif file_choice == "2":
        print("Для обработки выбран CSV-файл.")
        data = read_csv_file("data/transactions.csv")
    elif file_choice == "3":
        print("Для обработки выбран XLSX-файл.")
        data = read_excel_file("data/transactions_excel.xlsx")
    else:
        print("Неверный выбор. Выберите 1, 2 или 3.")
        return

    if not data:
        print("Не удалось загрузить данные из файла.")
        return

    # Фильтр по статусу
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input().strip().upper()

        filtered_by_status = filter_by_state(data, status)
        if filtered_by_status:
            print(f'Операции отфильтрованы по статусу "{status.upper()}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    # Сортировка по дате
    sort_operation_by_date = input("Отсортировать операции по дате? Да/Нет ").strip().lower()
    if sort_operation_by_date == "да":
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        ascending = order in ["по убыванию", "убыванию"]
        filtered_by_status = sort_by_date(filtered_by_status, ascending)
        # print(filtered_by_status)
    # Фильтр по рублям
    ruble_filter = input("Выводить только рублевые транзакции? Да/Нет ").strip().lower()
    if ruble_filter == "да":
        filtered_by_status = list(filter_by_currency(filtered_by_status, "RUB"))
    # print(filtered_by_status)

    # Поиск по слову в описании
    search_word = input("Отфильтровать список транзакций по определённому слову в описании? Да/Нет ").strip().lower()
    if search_word == "да":
        word = input("Введите слово для поиска в описании: ").strip()
        filtered_by_status = list(process_bank_search(filtered_by_status, word))

    # Вывод результатов
    print("Распечатываю итоговый список транзакций...\n")
    if not filtered_by_status:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(list(filtered_by_status))}\n")
        for transaction in filtered_by_status:
            date_str = get_date(transaction["date"])
            description = transaction.get("description", "")
            from_field = str(transaction.get("from", ""))
            to_field = str(transaction.get("to", ""))
            masked_from = mask_account_card(from_field)
            masked_to = mask_account_card(to_field)
            amount, currency = get_operation_amount(transaction)
            currency = transaction.get("operationAmount", {}).get("currency", {}).get("name", "")
            print(
                f"{date_str} {description}\n"
                f"{masked_from} -> {masked_to}\n"
                f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
