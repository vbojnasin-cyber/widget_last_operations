from pathlib import Path

from src.decorators import log

if __name__ == "__main__":

    # Временный файл для проверки записи на диск
    DIR_NAME = Path(__file__).parent
    FILE_DIR = DIR_NAME / "data" / "logs.txt"
    str_file = str(FILE_DIR)

    @log(filename=str_file)
    def process_payment(num: int, num_2: int) -> str:
        """Функция с файлом и kwargs — логирует успех в файл."""
        return num / num_2


print(log(process_payment(10, 0)))
