import pytest
from src.generators import filter_by_currency, transaction_descriptions


def test_filter_by_currency_success(data_transactions):
    """Тест успешной фильтрации транзакций."""
    assert filter_by_currency(data_transactions, "RUB") == [{
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    }]


@pytest.mark.parametrize(
    "invalid_data, currency, expected_error_msg",
    [
        ([], "RUB", "Вы ничего не передали"),
        ([{"id": 1}], "", "Вы ничего не передали"),
        ("not a list", "USD", "Ошибка передачи данных, вы передали не список"),
        ([{"id": 1}, "not a dict"], "EUR", "Ошибка передачи данных"),
        ([{"f"}, {}], "RUB", "Ошибка передачи данных"),  # Ваша изначальная проверка с множеством {"f"}
    ],
)
def test_filter_by_currency_exceptions(invalid_data, currency, expected_error_msg):
    """Параметризованный тест для проверки всех типов ValueError."""
    with pytest.raises(ValueError) as exc_info:
        filter_by_currency(invalid_data, currency)

    assert str(exc_info.value) == expected_error_msg

def test_filter_by_currency_no_match(data_transactions):
    """Тест ситуации, когда код валюты валиден, но совпадений нет."""
    assert filter_by_currency(data_transactions, "EUR") == []
#Тесты для transaction_descriptions
def test_valid_transaction_descriptions(data_transactions):
    assert transaction_descriptions(data_transactions) == ["Перевод организации", "Перевод со счета на счет"]
def test_empty_list_transaction_descriptions():
    with pytest.raises(ValueError):
        transaction_descriptions([])