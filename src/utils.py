import json
from pathlib import Path
from typing import Any, List


def read_file_json(filename: str) -> List[dict[str, Any]]:
    """Функция реализует чтение JSON-Файла"""
    path_obj = Path(filename)
    if not path_obj.is_file():
        return []
    try:
        with open(path_obj, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data
    except (json.JSONDecodeError, PermissionError):
        return []
    return []
