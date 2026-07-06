import pytest

from src.generators import (
    filter_by_currency,
    number_card_generator,
    transaction_descriptions,
)

# Test for the func filter_by_currency

def test_filter_by_currency_success():
    """Тест успешной фильтрации транзакций по валюте USD."""
    transactions = [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 2, "operationAmount": {"currency": {"code": "RUB"}}},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}},
    ]
    result = list(filter_by_currency(transactions, "USD"))

    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_filter_by_currency_not_found():
    """Тест возврата пустого генератора, если валюта не найдена."""
    transactions = [{"id": 1, "operationAmount": {"currency": {"code": "RUB"}}}]
    result = list(filter_by_currency(transactions, "EUR"))
    assert result == []


def test_filter_by_currency_both_empty():
    """Тест генерации ошибки при пустом списке и пустой строке валюты."""
    with pytest.raises(ValueError) as exc_info:
        list(filter_by_currency([], ""))
    assert "Вы ничего не передали" in str(exc_info.value)


def test_filter_by_currency_not_a_list():
    """Тест генерации ошибки, если вместо списка передан другой тип."""
    with pytest.raises(ValueError) as exc_info:
        list(filter_by_currency("not a list", "USD"))
    assert "Ошибка передачи данных, вы передали не список" in str(exc_info.value)


def test_filter_by_currency_not_a_dict():
    """Тест генерации ошибки, если элемент списка не является словарем."""
    with pytest.raises(ValueError) as exc_info:
        list(filter_by_currency([{"id": 1}, "not a dict"], "USD"))
    assert "Ошибка передачи данных" in str(exc_info.value)



# tests for the func transaction_descriptions


def test_transaction_descriptions_success():
    """Тест успешного извлечения существующих описаний транзакций."""
    transactions = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод частному лицу"},
        {"id": 3, "description": ""},  # Пустое описание должно проигнорироваться
    ]
    result = list(transaction_descriptions(transactions))
    assert result == ["Перевод организации", "Перевод частному лицу"]


def test_transaction_descriptions_empty():
    """Тест генерации ошибки при передаче пустого списка."""
    with pytest.raises(ValueError) as exc_info:
        list(transaction_descriptions([]))
    assert "Передали пустую транзакцию" in str(exc_info.value)


def test_transaction_descriptions_not_list():
    """Тест генерации ошибки, если передан не список."""
    with pytest.raises(ValueError) as exc_info:
        list(transaction_descriptions({"id": 1}))
    assert "Ошибка передачи данных, передали не тот тип" in str(exc_info.value)


def test_transaction_descriptions_not_dict():
    """Тест генерации ошибки, если внутри списка лежит не словарь."""
    with pytest.raises(ValueError) as exc_info:
        list(transaction_descriptions(["string_instead_of_dict"]))
    assert "Ошибка данных, передали не слоаврь" in str(exc_info.value)



#  test for the number_card_generator


def test_number_card_generator_success():
    """Тест корректной генерации номеров карт в заданном диапазоне с форматированием."""
    result = list(number_card_generator(1, 3))

    assert len(result) == 3
    assert result[0] == "0000 0000 0000 0001"
    assert result[1] == "0000 0000 0000 0002"
    assert result[2] == "0000 0000 0000 0003"


@pytest.mark.parametrize(
    "start, end",
    [
        (0, 10),  # start меньше 1
        (1, 10000000000000000),  # end больше 9999999999999999
        (10, 5),  # start больше end
    ]
)
def test_number_card_generator_invalid_range(start, end):
    """Тест генерации ошибки при некорректных границах диапазона."""
    with pytest.raises(ValueError) as exc_info:
        list(number_card_generator(start, end))
    assert "Неправильно заданы значения" in str(exc_info.value)