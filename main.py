from src.csv_excel_reader import read_csv_file
from src.csv_excel_reader import read_excel_file


def main() -> None:
    print(read_csv_file("data/transactions.csv"))
    print(read_excel_file("data/transactions_excel.xlsx"))


if __name__ == '__main__':
    main()
