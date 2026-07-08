import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv

from src import loggers

load_dotenv()

name = Path(__file__).stem
file_name = f"{name}.log"
logger = loggers.create_logger(name, file_name, logging.DEBUG)

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}


def get_connection():
    """Открывает соединение с PostgreSQL по параметрам из .env"""
    if not DB_CONFIG["dbname"] or not DB_CONFIG["user"]:
        error_msg = "Не заданы параметры подключения к БД (DB_NAME/DB_USER) в .env"
        logger.error(error_msg)
        raise ValueError(error_msg)
    try:
        return psycopg2.connect(**DB_CONFIG)
    except psycopg2.OperationalError as e:
        logger.error(f"Не удалось подключиться к БД: {e}")
        raise


def create_table() -> None:
    """Создаёт таблицу transactions, если её ещё нет"""
    query = """
    CREATE TABLE IF NOT EXISTS transactions (
        row_id SERIAL PRIMARY KEY,
        operation_id BIGINT,
        state VARCHAR(20),
        date TIMESTAMP,
        description TEXT,
        amount NUMERIC(20, 2),
        currency VARCHAR(10)
    );
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
        conn.commit()
    logger.info("Таблица transactions создана либо уже существовала")


def _prepare_row(transaction: Dict[str, Any]) -> Optional[tuple]:
    """Приводит одну транзакцию (в формате словаря из JSON/CSV/XLSX) к кортежу для вставки"""
    try:
        operation_amount = transaction.get("operationAmount", {})
        amount = operation_amount.get("amount")
        currency = operation_amount.get("currency", {}).get("code")

        return (
            transaction.get("id"),
            transaction.get("state"),
            transaction.get("date"),
            transaction.get("description"),
            amount,
            currency,
        )
    except AttributeError:
        logger.error(f"Некорректный формат транзакции, пропускаю: {transaction}")
        return None


def save_transactions(transactions: List[Dict[str, Any]]) -> int:
    """Сохраняет список транзакций в таблицу transactions.

    Возвращает количество реально вставленных строк.
    """
    if not transactions:
        logger.info("Список транзакций пуст, сохранять нечего")
        return 0

    rows = [row for row in (_prepare_row(t) for t in transactions) if row is not None]

    if not rows:
        return 0

    query = """
        INSERT INTO transactions (operation_id, state, date, description, amount, currency)
        VALUES %s
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            execute_values(cur, query, rows)
        conn.commit()

    logger.info(f"Сохранено {len(rows)} транзакций в БД")
    return len(rows)


