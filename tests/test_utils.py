import json
from unittest.mock import patch
from src.utils import read_file_json




# pozitive test


def test_read_file_json_success(tmp_path):
    """Тест успешного чтения валидного JSON-файла со списком словарей."""
    test_file = tmp_path / "valid.json"
    expected_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    test_file.write_text(json.dumps(expected_data), encoding="utf-8")

    result = read_file_json(str(test_file))
    assert result == expected_data


# negative test

def test_read_file_json_not_a_file(tmp_path):
    """Тест возврата пустого списка, если переданный путь не является файлом (например, это папка)."""
    result = read_file_json(str(tmp_path))
    assert result == []


def test_read_file_json_invalid_json(tmp_path):
    """Тест возврата пустого списка при битом/невалидном JSON-файле (JSONDecodeError)."""
    test_file = tmp_path / "broken.json"
    test_file.write_text("{'invalid_json': True", encoding="utf-8")  # некорректный синтаксис JSON

    result = read_file_json(str(test_file))
    assert result == []


def test_read_file_json_not_a_list(tmp_path):
    """Тест возврата пустого списка, если JSON валидный, но внутри объект (dict), а не список (list)."""
    test_file = tmp_path / "dict.json"
    test_file.write_text(json.dumps({"key": "value"}), encoding="utf-8")

    result = read_file_json(str(test_file))
    assert result == []


def test_read_file_json_permission_error(tmp_path):
    """Тест возврата пустого списка при ошибке доступа к файлу (PermissionError)."""
    test_file = tmp_path / "protected.json"
    test_file.write_text("[]", encoding="utf-8")

    with patch("builtins.open", side_effect=PermissionError):
        result = read_file_json(str(test_file))
        assert result == []
