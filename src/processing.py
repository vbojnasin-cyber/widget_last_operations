from typing import List


def filter_by_state(*, data: List[dict], state: str = "EXECUTED") -> List[dict]:
    """Сортирует транзакции по состоянию state"""
    if not data:
        return []
    if not isinstance(data, list):
        raise ValueError(f"Ожидалось получение списка, а получен {type(data)}")
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Получен не словарь")
    return [item for item in data if item.get("state") == state]


def sort_by_date(transactions: List[dict], reverse: bool = True):
    """Сортирует транзакции по дате"""
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
