import re
from typing import Any, Dict, List


def process_bank_search(
    data: List[Dict[str, Any]], search_string: str
) -> List[Dict[str, Any]]:
    """Фильтрует операции, находя подстроку в поле 'description' через регулярные выражения."""
    if not search_string:
        return data

    filtered_data: List[Dict[str, Any]] = []

    try:
        pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    except re.error:
        return []

    for operation in data:
        description = operation.get("description")
        if isinstance(description, str) and pattern.search(description):
            filtered_data.append(operation)

    return filtered_data


def process_bank_operations(
    data: List[Dict[str, Any]], categories: List[str]
) -> Dict[str, int]:
    """Считает количество операций для каждой категории из переданного списка."""

    category_counts: Dict[str, int] = {category: 0 for category in categories}

    for operation in data:
        description = operation.get("description")

        if isinstance(description, str) and description in category_counts:
            category_counts[description] += 1

    return category_counts
