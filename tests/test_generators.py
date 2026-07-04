import pytest

from src.generators import (
    filter_by_currency,
    number_card_generator,
    transaction_descriptions,
)

# Test for the func filter_by_currency


# 1 test
def test_filter_by_currency_success(data_transactions):
    """Успешная фильтрация по валюте"""
    result = list(filter_by_currency(data_transactions, "RUB"))
    assert len(result) == 1
    assert result[0]["id"] == 873106923


# 2 test
def test_filter_by_currency_no_match(data_transactions):
    """Проверка на поиск несуществующей валюты в транзакциях"""
    result = list(filter_by_currency(data_transactions, "EUR"))
    assert result == []


# 3 test
def test_filter_by_currency_dict():
    """Проверка ошибки, на вхождения аргуменета, который не является списком словарей"""
    with pytest.raises(ValueError):
        list(filter_by_currency({}, ""))


# Test for the func transaction_descriptions


# 1 test
def test_transaction_descriptiopns_valid(data_transactions):
    """Успешная работа функции с валидными данными"""
    result = transaction_descriptions(data_transactions)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"


# 2 test
def test_transaction_descriptions():
    """Проверка вывода описания, когда у транзакции описание отсутсвует"""
    result = list(transaction_descriptions([{"id": 1234234}, {"name": "vlad"}]))
    assert result == []


# Test for the func number_card_generator


# 1 test
def test_number_card_generator_error():
    """Проверка ошибки при невалидных данных"""
    with pytest.raises(ValueError):
        result = number_card_generator(0, 0)
        next(result)


# 2 test
def test_number_card_generator_valid():
    """Проверка генератора при валидных данных"""
    result = number_card_generator(1, 100)
    assert next(result) == "0000 0000 0000 0001"
