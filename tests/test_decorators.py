import pytest

from src.decorators import log


def test_log_in_console(capsys):
    """Тест вывода в консоль"""

    @log()
    def exampl_func(x, y):
        return x * y

    exampl_func(2, 3)
    captured = capsys.readouterr()
    assert captured.out == "exampl_func ok\n"


def test_log_to_console_except(capsys):
    """Тест вывода в консоль при исключении"""

    @log()
    def func(x):
        raise ValueError("Error!")

    with pytest.raises(ValueError, match="Error!"):
        func(5)

    captured = capsys.readouterr()
    assert "func error: Error!" in captured.out


def test_log_in_file(tmp_path):
    """Тест записи в лог файл"""
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def exampl_func(x, y):
        return x * y

    exampl_func(2, 4)
    assert log_file.read_text() == "exampl_func ok\n"
