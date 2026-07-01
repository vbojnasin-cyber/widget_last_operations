from typing import List, Dict
def filter_by_currency(data_list: List[Dict], currency: str) -> List[Dict]:
    """Фильтрует список транзакций по указанному коду валюты."""
    if not data_list or not currency:
        raise ValueError("Вы ничего не передали")
    # Проверяю, что передан именно список
    if not isinstance(data_list, list):
        raise ValueError("Ошибка передачи данных, вы передали не список")
    # Проверяю, что вcе элементы внутри словари
    for data in data_list:
        if not isinstance(data, dict):
            raise ValueError("Ошибка передачи данных")
    # Фильтрация транзакции (благодаря .get() она полностью безопасна)
    return [
        transaction for transaction in data_list
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency
    ]
def transaction_descriptions(transactions: List[dict]) -> List[str]:
    if not transactions:
        raise ValueError("Передали пустую транзакцию")
    if not isinstance(transactions, list):
        raise ValueError("Ошибка передачи данных, передали не тот тип")
    """Функция фильтрует транзакции по описанию переводов"""
    return [transaction["description"] for transaction in transactions if transaction.get("description")]

