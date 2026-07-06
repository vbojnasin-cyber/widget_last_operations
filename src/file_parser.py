import json
import logging
import math
from pathlib import Path
from typing import Union, List, Any, Dict
import pandas as pd

from src import loggers

FILE = Path(__file__).resolve().parent.parent
FILE_DIR = FILE / "data" / "transactions_excel.xlsx"
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


def load_operations_from_csv(file_path: Union[str, Path]) -> pd.DataFrame:
    """Считывает транзакции из CSV.

    Генерирует ошибки, если файл отсутствует или поврежден.
    """
    path_obj = Path(file_path)
    if not path_obj.is_file():
        raise FileNotFoundError(f"Критическая ошибка: Файл не найден по пути {path_obj}")

    try:
        df = pd.read_csv(path_obj, sep=";", encoding="utf-8")
        df.columns = [str(col).strip().lower() for col in df.columns]
        return df
    except Exception as e:
        raise ValueError(f"Не удалось распарсить CSV-файл: {e}") from e


def load_operations_from_xls(file_path: Union[str, Path]) -> pd.DataFrame:
    """Считывает транзакции из XLSX.
    Генерирует ошибки, если файл отсутствует или поврежден.
    """
    path_obj = Path(file_path)
    if not path_obj.is_file():
        raise FileNotFoundError(f"Критическая ошибка: Файл не найден по пути {path_obj}")

    try:
        df = pd.read_excel(path_obj, engine="openpyxl")
        df.columns = [str(col).strip().lower() for col in df.columns]
        return df
    except Exception as e:
        raise ValueError(f"Не удалось распарсить Excel-файл: {e}") from e


def dataframe_to_transactions(df: pd.DataFrame) -> List[Dict[str, Any]]:
    """Приводит DataFrame (из CSV/XLSX с плоскими колонками) к тому же формату
    словарей, что и данные из JSON, чтобы processing/generators/utils/widget
    могли работать с транзакциями из любого источника одинаково.

    Ожидаемые колонки в CSV/XLSX (после нормализации в load_operations_from_*):
    id, state, date, amount, currency_name, currency_code, from, to, description
    """
    transactions: List[Dict[str, Any]] = []

    for _, row in df.iterrows():
        row_dict = row.to_dict()

        def clean(value: Any) -> Any:
            if isinstance(value, float) and math.isnan(value):
                return None
            return value

        transaction = {
            "id": clean(row_dict.get("id")),
            "state": clean(row_dict.get("state")),
            "date": clean(row_dict.get("date")),
            "operationAmount": {
                "amount": clean(row_dict.get("amount")),
                "currency": {
                    "name": clean(row_dict.get("currency_name")),
                    "code": clean(row_dict.get("currency_code")),
                },
            },
            "from": clean(row_dict.get("from")),
            "to": clean(row_dict.get("to")),
            "description": clean(row_dict.get("description")),
        }
        transactions.append(transaction)

    return transactions

