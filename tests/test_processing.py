import pytest
from src.processing import filter_by_state, sort_by_date
# Test for the filter_by_state func
class TestFilterByState:
    # 1 test
    def test_default_state_executed(self, test_data):
        """По умолчанию фильтрует EXECUTED."""
        result = filter_by_state(data=test_data)
        assert result == [
            {"id": 1, "state": "EXECUTED"},
            {"id": 3, "state": "EXECUTED"},
        ]

    # 2 test
    def test_custom_state(self, test_data):
        """Фильтр по переданному state."""
        result = filter_by_state(data=test_data, state="CANCELED")
        assert result == [{"id": 2, "state": "CANCELED"}]

    # 3 test
    def test_empty_list_returns_empty(self):
        """Пустой список = пустой список."""
        assert filter_by_state(data=[]) == []

    # 4 test
    def test_no_matches_returns_empty(self, test_data):
        """Ничего не подошло, пустой список."""
        assert filter_by_state(data=test_data, state="PENDING") == []

    # 5 test
    def test_missing_state_key_ignored(self):
        """Словарь без ключа state игнорируется."""
        data = [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "amount": 100},  # нет state
        ]
        result = filter_by_state(data=data)
        assert result == [{"id": 1, "state": "EXECUTED"}]

    # 6 test
    def test_case_sensitive(self):
        """EXECUTED != executed (проверяем, что регистр важен)."""
        data = [{"id": 1, "state": "executed"}]
        result = filter_by_state(data=data, state="EXECUTED")
        assert result == []

    # 7 test
    def test_input_is_not_list_raises(self):
        """Передали не список ValueError."""
        with pytest.raises(ValueError):
            filter_by_state(data="i not list")

    # 8 test
    def test_input_list_contains_not_dict_raises(self):
        """В списке не словарь  ValueError."""
        with pytest.raises(ValueError):
            filter_by_state(data=["string", 123])


# Test for the sort_by_date func
class TestSortByDate:

    # 1 test
    def test_default_descending(self):
        """По умолчанию сортирует по убыванию."""
        data = [
            {"id": 1, "date": "2024-01-01"},
            {"id": 2, "date": "2024-03-15"},
            {"id": 3, "date": "2024-01-10"},
        ]
        result = sort_by_date(data)
        assert result == [
            {"id": 2, "date": "2024-03-15"},
            {"id": 3, "date": "2024-01-10"},
            {"id": 1, "date": "2024-01-01"},
        ]

    # 2 test
    def test_ascending_order(self):
        """reverse=False по возрастанию."""
        data = [
            {"id": 1, "date": "2024-01-01"},
            {"id": 2, "date": "2024-03-15"},
        ]
        result = sort_by_date(data, reverse=False)
        assert result == [
            {"id": 1, "date": "2024-01-01"},
            {"id": 2, "date": "2024-03-15"},
        ]

    # 3 test
    def test_same_date_preserves_order(self):
        """Одинаковые даты порядок сохраняется."""
        data = [
            {"id": 1, "date": "2024-01-01"},
            {"id": 2, "date": "2024-01-01"},
        ]
        result = sort_by_date(data)
        assert result == [
            {"id": 1, "date": "2024-01-01"},
            {"id": 2, "date": "2024-01-01"},
        ]

    # 4 test
    def test_empty_list(self):
        """Пустой список пустой список."""
        assert sort_by_date([]) == []

    # 5 test
    def test_single_item(self):
        """Один элемент тот же список."""
        data = [{"id": 1, "date": "2024-01-01"}]
        assert sort_by_date(data) == data
