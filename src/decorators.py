from functools import wraps
from typing import Any
from typing import Callable
from typing import Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования выполнения функции.
    Если задан `filename`, лог записывается в файл, иначе выводится в консоль."""

    def decorator(func: Callable) -> Callable:
        """Возвращает обёртку, которая логирует выполнение функции `func`."""

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Обёртка для выполнения функции `func` с логированием её результата и ошибок."""
            message = ""
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok\n"

            except Exception as e:
                message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
                raise e

            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message)
                else:
                    print(message)
            return result

        return wrapper

    return decorator
