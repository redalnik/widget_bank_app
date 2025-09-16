import requests
from dotenv import load_dotenv
import os
from typing import Dict
# import json   # для тестирования
# from src.utils import load_transactions # для тестирования

load_dotenv()
API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")
url = "https://api.apilayer.com/exchangerates_data/convert"


def transaction_amount(transaction: Dict) -> float:
    """Возвращает сумму транзакции в рублях. Если валюта транзакции отличается от рубля,
    производится конвертация через внешний API."""
    try:
        # Извлекаем данные из файла транзакций operations.json
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"].upper()

        # Рубли возвращаем как есть
        if currency == "RUB":
            return amount

        # Проверка на наличие API ключа
        if not API_KEY:
            raise EnvironmentError("API ключ не найден в переменных окружения.")

        # Конвертация в РУБ.
        params = {"to": "RUB", "from": currency, "amount": amount}

        headers = {"apikey": API_KEY}
        response = requests.request("GET", url, params=params, headers=headers, timeout=5)

        if response.status_code == 200:
            result = response.json()
            return float(result["result"])
        else:
            raise RuntimeError(f"Ошибка ответа сервера: статус-код {response.status_code}")

    except KeyError as ke:
        print(f"Ошибка, отсутствует ключ {ke}")
        return 0.0
    except ValueError:
        print("Ошибка преобразования суммы")
        return 0.0
    except Exception as ex:
        print(f"Общая ошибка: {ex}")
        return 0.0


# if __name__ == '__main__':
#     transactions = load_transactions("../data/operations.json")
#     print(f"Сумма транзакции в рублях: {transaction_amount(transactions[0]):.2f}")
#     print(f"Сумма транзакции в рублях: {transaction_amount(transactions[1]):.2f}")
#     print(f"Сумма транзакции в рублях: {transaction_amount(transactions[2]):.2f}")
#     print(f"Сумма транзакции в рублях: {transaction_amount(transactions[3]):.2f}")
