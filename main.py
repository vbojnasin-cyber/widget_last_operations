"""Главный модуль программы работы с банковскими транзакциями.
Связывает функциональность file_parser, processing, generators,
utils и widget в единый пользовательский сценарий."""

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from src.file_parser import (
    read_file_json,
    load_operations_from_csv,
    load_operations_from_xls,
    dataframe_to_transactions,
)
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.utils import process_bank_search
from src.widget import mask_account_card
from src.bd import create_table, save_transactions

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

JSON_FILE = DATA_DIR / "operations.json"
CSV_FILE = DATA_DIR / "transactions.csv"
XLSX_FILE = DATA_DIR / "transactions_excel.xlsx"

AVAILABLE_STATUSES = ("EXECUTED", "CANCELED", "PENDING")

PREVIEW_COUNT = 5


def get_transactions_by_choice(choice: str) -> List[Dict[str, Any]]:
    """Загружает транзакции в зависимости от выбранного пользователем источника
    и приводит их к единому формату словарей (как в JSON)."""
    if choice == "1":
        print("\nДля обработки выбран JSON-файл.")
        return read_file_json(str(JSON_FILE))

    if choice == "2":
        print("\nДля обработки выбран CSV-файл.")
        df = load_operations_from_csv(CSV_FILE)
        return dataframe_to_transactions(df)

    if choice == "3":
        print("\nДля обработки выбран XLSX-файл.")
        df = load_operations_from_xls(XLSX_FILE)
        return dataframe_to_transactions(df)

    return []


def ask_menu_choice() -> str:
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )
    while True:
        choice = input("Пользователь: ").strip()
        if choice in ("1", "2", "3"):
            return choice
        print("Неверный пункт меню, попробуйте снова (1, 2 или 3).")


def ask_status_filter() -> str:
    while True:
        print(
            "\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        status = input("Пользователь: ").strip().upper()
        if status in AVAILABLE_STATUSES:
            print(f'\nОперации отфильтрованы по статусу "{status}"')
            return status
        print(f'\nСтатус операции "{status}" недоступен.')


def ask_yes_no(question: str) -> bool:
    while True:
        print(f"\n{question} Да/Нет")
        answer = input("Пользователь: ").strip().lower()
        if answer in ("да", "yes", "y", "д"):
            return True
        if answer in ("нет", "no", "n", "н"):
            return False
        print("Пожалуйста, ответьте 'Да' или 'Нет'.")


def ask_sort_order() -> bool:
    """Возвращает True, если нужно сортировать по убыванию (reverse=True)."""
    while True:
        print("\nОтсортировать по возрастанию или по убыванию?")
        answer = input("Пользователь: ").strip().lower()
        if "возраст" in answer:
            return False
        if "убыв" in answer:
            return True
        print("Пожалуйста, ответьте 'по возрастанию' или 'по убыванию'.")


def format_date(raw_date: Any) -> str:
    """Приводит дату транзакции к формату ДД.ММ.ГГГГ, независимо от того,
    в каком виде она пришла (ISO-строка из JSON, datetime из pandas)."""
    if isinstance(raw_date, datetime):
        return raw_date.strftime("%d.%m.%Y")

    if raw_date is None:
        return ""

    date_str = str(raw_date)
    formats = (
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
        "%d.%m.%Y",
    )
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).strftime("%d.%m.%Y")
        except ValueError:
            continue
    return date_str


def format_account_or_card(value: Any) -> str:
    """Маскирует номер счета/карты через widget.mask_account_card.
    Если значение пустое или не поддается маскированию - возвращает как есть."""
    if not value:
        return ""
    try:
        return mask_account_card(str(value))
    except ValueError:
        return str(value)


def format_amount(amount: Any) -> str:
    """Приводит сумму к аккуратному виду: целые числа без .0,
    дробные - максимум с двумя знаками после точки."""
    try:
        value = float(amount)
    except (TypeError, ValueError):
        return str(amount)
    if value.is_integer():
        return str(int(value))
    return f"{value:.2f}"


def print_transaction(transaction: Dict[str, Any]) -> None:
    date = format_date(transaction.get("date"))
    description = transaction.get("description") or ""
    from_value = transaction.get("from")
    to_value = transaction.get("to")

    if from_value:
        accounts_line = f"{format_account_or_card(from_value)} -> {format_account_or_card(to_value)}"
    else:
        accounts_line = format_account_or_card(to_value)

    operation_amount = transaction.get("operationAmount", {}) or {}
    amount = format_amount(operation_amount.get("amount", ""))
    currency_code = (operation_amount.get("currency") or {}).get("code", "")
    currency_display = "руб." if currency_code == "RUB" else currency_code

    print(f"{date} {description}")
    if accounts_line:
        print(accounts_line)
    print(f"Сумма: {amount} {currency_display}\n")


def main() -> None:
    choice = ask_menu_choice()
    transactions = get_transactions_by_choice(choice)

    status = ask_status_filter()
    transactions = filter_by_state(data=transactions, state=status)

    if ask_yes_no("Отсортировать операции по дате?"):
        reverse = ask_sort_order()
        transactions = sort_by_date(transactions, reverse=reverse)

    if ask_yes_no("Выводить только рублевые транзакции?"):
        transactions = list(filter_by_currency(transactions, "RUB"))

    if ask_yes_no("Отфильтровать список транзакций по определенному слову в описании?"):
        print("\nВведите слово или фразу для поиска в описании:")
        search_word = input("Пользователь: ").strip()
        transactions = process_bank_search(transactions, search_word)

    if not transactions:
        print(
            "\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации"
        )
        return

    print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")

    preview = transactions[:PREVIEW_COUNT]
    rest = transactions[PREVIEW_COUNT:]

    print(f"Показываю первые {len(preview)} операций для примера...\n")
    for transaction in preview:
        print_transaction(transaction)

    print(f"Остальные {len(rest)} операций сохраняю в базу данных...")
    create_table()
    saved_count = save_transactions(rest)
    print(f"Сохранено в БД: {saved_count} операций.")


if __name__ == "__main__":
    main()