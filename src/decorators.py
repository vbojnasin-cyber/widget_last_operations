from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                writing_to_file(message, filename)
                return result
            except Exception as e:
                message = f"{func.__name__} Ошибка: {e}. Входящие аргументы  = {args}, {kwargs}"
                writing_to_file(message, filename)
                raise

        return wrapper

    return decorator


def writing_to_file(message: str, filename: Optional[str] = None) -> None:
    """Функция для записи сообщений в файл или в консоль"""
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)
