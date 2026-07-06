import pytest
from src.processing import filter_by_state, sort_by_date
# Test for the filter_by_state func
def test_filter_by_state_default(sample_transactions):
    """Тест фильтрации по состоянию EXECUTED (значение по умолчанию)."""
    result = filter_by_state(data=sample_transactions)
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_filter_by_state_custom(sample_transactions):
    """Тест фильтрации по кастомному состоянию (например, CANCELED)."""
    result = filter_by_state(data=sample_transactions, state="CANCELED")
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_filter_by_state_empty():
    """Тест возврата пустого списка, если на вход передан пустой список."""
    assert filter_by_state(data=[]) == []


def test_filter_by_state_not_found(sample_transactions):
    """Тест возврата пустого списка, если искомого состояния нет в данных."""
    result = filter_by_state(data=sample_transactions, state="NON_EXISTENT")
    assert result == []


@pytest.mark.parametrize("bad_data", [123, "not a list", {"key": "val"}, None])
def test_filter_by_state_invalid_input_type(bad_data):
    """Тест генерации ошибки, если передан не список."""
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(data=bad_data)
    assert "Ожидалось получение списка" in str(exc_info.value)


def test_filter_by_state_invalid_element_type():
    """Тест генерации ошибки, если внутри списка находится не словарь."""
    invalid_data = [{"id": 1, "state": "EXECUTED"}, "not a dict", {"id": 2}]
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(data=invalid_data)
    assert "Получен не словарь" in str(exc_info.value)



# TEst for the sort_by_date


def test_sort_by_date_descending(sample_transactions):
    """Тест сортировки по дате от самых новых к самым старым (по умолчанию)."""
    result = sort_by_date(sample_transactions)
    assert [item["id"] for item in result] == [2, 4, 1, 3]


def test_sort_by_date_ascending(sample_transactions):
    """Тест сортировки по дате от самых старых к самым новым (reverse=False)."""
    result = sort_by_date(sample_transactions, reverse=False)
    assert [item["id"] for item in result] == [3, 1, 4, 2]


def test_sort_by_date_empty():
    """Тест сортировки пустого списка (должен вернуть пустой список)."""
    assert sort_by_date([]) == []