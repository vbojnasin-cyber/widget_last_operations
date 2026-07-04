from typing import Dict, Iterator, List


def filter_by_currency(data_list: List[Dict], currency: str) -> Iterator[Dict]:
    """Фильтрует список транзакций по указанному коду валюты."""
    if not data_list and not currency:
        raise ValueError("Вы ничего не передали")

    if not isinstance(data_list, list):
        raise ValueError("Ошибка передачи данных, вы передали не список")

    for data in data_list:
        if not isinstance(data, dict):
            raise ValueError("Ошибка передачи данных")

        if data.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield data


def transaction_descriptions(transactions: List[dict]) -> Iterator[Dict]:
    """Функция фильтрует транзакции по описанию переводов"""
    if not transactions:
        raise ValueError("Передали пустую транзакцию")

    if not isinstance(transactions, list):
        raise ValueError("Ошибка передачи данных, передали не тот тип")

    for transaction in transactions:
        if not isinstance(transaction, dict):
            raise ValueError("Ошибка данных, передали не слоаврь")

        if transaction.get("description", ""):
            yield transaction["description"]


def number_card_generator(start: int, end: int) -> Iterator[str]:
    """Генератор номеров банковских кард"""
    if start < 1 or end > 9999999999999999 or start > end:
        raise ValueError("Неправильно заданы значения")
    for number in range(start, end + 1):
        card_str = f"{number:016d}"
        card_number = (
            f"{card_str[0:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
        )
        yield card_number
