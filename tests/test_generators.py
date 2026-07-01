import pytest

from src.generators import (
    filter_by_currency,
    number_card_generator,
    transaction_descriptions,
)


# 3 Базовых теста для filter_by_currency
def test_filter_by_currency_success(data_transactions):
    """Успешная фильтрация по валюте"""
    result = list(filter_by_currency(data_transactions, "RUB"))
    assert len(result) == 1
    assert result[0]["id"] == 873106923


def test_filter_by_currency_no_match(data_transactions):
    result = list(filter_by_currency(data_transactions, "EUR"))
    assert result == []


def test_filter_by_currency_dict():
    with pytest.raises(ValueError):
        list(filter_by_currency({}, ""))


# Базовые тесты для transaction_descriptions
def test_transaction_descriptiopns_valid(data_transactions):
    result = transaction_descriptions(data_transactions)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"


def test_transaction_descriptions():
    result = list(transaction_descriptions([{"id": 1234234}, {"name": "vlad"}]))
    assert result == []


# Базовые тесты для генератора номеров карт
def test_number_card_generator_error():
    with pytest.raises(ValueError):
        result = number_card_generator(0, 0)
        next(result)


def test_number_card_generator_valid():
    result = number_card_generator(1, 100)
    assert next(result) == "0000 0000 0000 0001"
