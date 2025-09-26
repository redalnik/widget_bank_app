from typing import List

import pandas as pd


def read_csv_file(file_path: str) -> List[dict]:
    """Функция для считывания финансовых операций из CSV и вывода списка словарей с транзакциями."""
    try:
        data_csv = pd.read_csv(file_path, delimiter=';')
        csv_dict = data_csv.to_dict(orient='records')
        return csv_dict
    except FileNotFoundError:
        print(f'Ошибка! Файл {file_path} не найден!')
        return []
    except Exception as e:
        print(f"Ошибка чтения CSV: {e}")
        return []


def read_excel_file(file_path: str) -> List[dict]:
    """Функция для считывания финансовых операций из EXCEL и вывода списка словарей с транзакциями."""
    try:
        data_excel = pd.read_excel(file_path)
        excel_dict = data_excel.to_dict(orient='records')
        return excel_dict
    except FileNotFoundError:
        print(f'Ошибка! Файл {file_path} не найден!')
        return []
    except Exception as e:
        print(f"Ошибка чтения EXCEL: {e}")
        return []
