import logging
from src import loggers
import json
from typing import Any, List
from pathlib import Path

name = Path(__file__).stem
file_name = f"{name}.log"
logger = loggers.create_logger(name, file_name, logging.DEBUG)

def read_file_json(filename: str) -> List[dict[str, Any]]:
    """Функция реализует чтение JSON-Файла"""
    path_obj = Path(filename)
    if not path_obj.is_file():
        error_msg = f"Вы передали не файл"
        logger.error(error_msg)
        return []
    logger.info(f"{filename} - Получен, следущий шаг распаковка")
    try:
        with open(path_obj, "r", encoding="utf-8") as file:
            data = json.load(file)


        if isinstance(data, list):
            logger.info("Файл успешно распакован")
            return data
    except (json.JSONDecodeError, PermissionError):
        logger.error("Файл поврежден или не содержит валидиных данных")
        return []
    return []
