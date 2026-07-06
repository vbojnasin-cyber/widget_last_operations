from src.decorators import log
import pytest

# test for the log and file_write
def test_log_console_success(capsys):
    """Тест успешного выполнения функции с выводом в консоль."""

    @log()
    def add(x, y):
        return x + y

    result = add(2, 3)

    assert result == 5
    captured = capsys.readouterr()
    assert captured.out.strip() == "add ok"


def test_log_console_error(capsys):
    """Тест перехвата ошибки функции с выводом в консоль."""

    @log()
    def divide(x, y):
        return x / y


    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide Ошибка: division by zero" in captured.out
    assert "Входящие аргументы  = (1, 0), {}" in captured.out


def test_log_file_success(tmp_path):
    """Тест успешного выполнения функции с записью в файл."""
    test_file = tmp_path / "test_success.log"

    @log(filename=str(test_file))
    def greet(name):
        return f"Hello, {name}"

    result = greet("Alice")
    assert result == "Hello, Alice"

    log_content = test_file.read_text(encoding="utf-8")
    assert log_content.strip() == "greet ok"



def test_log_file_error(tmp_path):
    """Тест записи информации об ошибке в файл."""
    test_file = tmp_path / "test_error.log"

    @log(filename=str(test_file))
    def process_data(data):
        return data["key"]

    with pytest.raises(KeyError):
        process_data({})

    log_content = test_file.read_text(encoding="utf-8")
    assert "process_data Ошибка:" in log_content
    assert "Входящие аргументы  = ({},), {}" in log_content