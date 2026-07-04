from src.decorators import log


# 1 test
def test_log_console_success(capsys):
    """Выполнение декоратора с выводом в консоль"""

    @log()
    def my_test_func(x, y):
        return x + 7

    my_test_func(1, 3)
    captured = capsys.readouterr()
    assert captured.out == "my_test_func ok\n"


# 2 test
def test_log_file_success(tmp_path):
    """Проверяет, что при успешном выполнении лог записывается в указанный файл."""
    log_file = tmp_path / "success.log"

    @log(filename=str(log_file))
    def greet(name):
        return f"Hello, {name}"

    greet("Alice")
    log_content = log_file.read_text(encoding="utf-8")
    assert log_content == "greet ok\n"
