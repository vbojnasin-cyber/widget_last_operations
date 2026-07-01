import pytest

from src.processing import filter_by_state, sort_by_date


# filter_by_state
class TestFilterByState:

    def test_default_state_executed(self):
        """По умолчанию фильтрует EXECUTED."""
        data = [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "CANCELED"},
            {"id": 3, "state": "EXECUTED"},
        ]
        result = filter_by_state(data)
        assert result == [
            {"id": 1, "state": "EXECUTED"},
            {"id": 3, "state": "EXECUTED"},
        ]

    def test_custom_state(self):
        """Фильтр по переданному state."""
        data = [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "CANCELED"},
        ]
        result = filter_by_state(data, state="CANCELED")
        assert result == [{"id": 2, "state": "CANCELED"}]

    def test_empty_list_returns_empty(self):
        """Пустой список = пустой список."""
        assert filter_by_state([]) == []

    def test_no_matches_returns_empty(self):
        """Ничего не подошло, пустой список."""
        data = [{"id": 1, "state": "CANCELED"}]
        assert filter_by_state(data, state="PENDING") == []

    def test_missing_state_key_ignored(self):
        """Словарь без ключа state игнорируется."""
        data = [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "amount": 100},  # нет state
        ]
        result = filter_by_state(data)
        assert result == [{"id": 1, "state": "EXECUTED"}]

    def test_case_sensitive(self):
        """EXECUTED != executed (проверяем, что регистр важен)."""
        data = [{"id": 1, "state": "executed"}]
        result = filter_by_state(data, state="EXECUTED")
        assert result == []

    def test_input_is_not_list_raises(self):
        """Передали не список ValueError."""
        with pytest.raises(ValueError):
            filter_by_state("i not list")

    def test_input_list_contains_not_dict_raises(self):
        """В списке не словарь  ValueError."""
        with pytest.raises(ValueError):
            filter_by_state(["string", 123])


# sort_by_date


class TestSortByDate:

    def test_default_descending(self):
        """По умолчанию сортирует по убыванию (новые первыми)."""
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

    def test_empty_list(self):
        """Пустой список пустой список."""
        assert sort_by_date([]) == []

    def test_single_item(self):
        """Один элемент тот же список."""
        data = [{"id": 1, "date": "2024-01-01"}]
        assert sort_by_date(data) == data
