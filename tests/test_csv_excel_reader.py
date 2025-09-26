from unittest.mock import Mock
from unittest.mock import patch

import pandas as pd

from src.csv_excel_reader import read_csv_file
from src.csv_excel_reader import read_excel_file


@patch("csv_excel_reader.pd.read_excel")
def test_read_excel_all_exception(mock_read):
    mock_read.side_effect = Exception
    result = read_excel_file("file.xlsx")
    assert result == []


@patch("csv_excel_reader.pd.read_excel")
def test_read_excel_file_not_found(mock_read):
    mock_read.side_effect = FileNotFoundError
    result = read_excel_file("file.xlsx")
    assert result == []
    mock_read.assert_called_once_with("file.xlsx")


@patch("csv_excel_reader.pd.read_excel")
def test_read_excel_to_dict(mock_read, csv_excel_file_return_index_0):
    mock_df = Mock()
    mock_df.to_dict.return_value = [csv_excel_file_return_index_0]
    mock_read.return_value = mock_df  # .pd.read_excel вернет [csv_excel_file_return_index_0]
    result = read_excel_file("file.xlsx")  # вернет список с одним словарем [csv_excel_file_return_index_0]
    assert result == [csv_excel_file_return_index_0]
    mock_read.assert_called_once_with("file.xlsx")


@patch("csv_excel_reader.pd.read_excel")
def test_read_excel_empty_file(mock_read):
    mock_read.return_value = pd.DataFrame()
    result = read_excel_file('empty.xlsx')
    assert result == []
    mock_read.assert_called_once_with('empty.xlsx')


def test_read_excel_file(csv_excel_file_return_index_0):
    data_excel = read_excel_file('./data/transactions_excel.xlsx')
    result = data_excel[0]
    assert result == csv_excel_file_return_index_0


@patch("csv_excel_reader.pd.read_csv")
def test_read_csv_file_not_found(mock_read):
    mock_read.side_effect = FileNotFoundError
    result = read_csv_file("file.csv")
    assert result == []
    mock_read.assert_called_once_with("file.csv", delimiter=';')


@patch("csv_excel_reader.pd.read_csv")
def test_read_csv_empty_file(mock_read):
    mock_read.return_value = pd.DataFrame()
    result = read_csv_file('empty.csv')
    assert result == []


def test_read_csv_file(csv_excel_file_return_index_0):
    data_csv = read_csv_file('./data/transactions.csv')
    result = data_csv[0]
    assert result == csv_excel_file_return_index_0


@patch("csv_excel_reader.pd.read_csv")
def test_read_csv_to_dict(mock_read, csv_excel_file_return_index_0):
    mock_df = Mock()
    mock_df.to_dict.return_value = [csv_excel_file_return_index_0]
    mock_read.return_value = mock_df  # .pd.read_csv вернет [csv_excel_file_return_index_0]
    result = read_csv_file("file.csv")  # вернет список с одним словарем [csv_excel_file_return_index_0]
    assert result == [csv_excel_file_return_index_0]
    mock_read.assert_called_once_with("file.csv", delimiter=';')


@patch("csv_excel_reader.pd.read_csv")
def test_read_csv_all_exception(mock_read):
    mock_read.side_effect = Exception
    result = read_csv_file("file.csv")
    assert result == []
