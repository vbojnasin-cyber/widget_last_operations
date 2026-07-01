import pytest
#Фикстуры для get_mask_card_number
@pytest.fixture
def test_small_number_card():
    return "11111"
@pytest.fixture
def test_name():
    return "1111111111111111"
@pytest.fixture
def test_num_and_sym_number_card():
    return "1233333333h33333"
#Фикстуры для generators.py
@pytest.fixture
def data_transactions():
    return [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                        "amount": "9824.07",
                        "currency": {
                            "name": "USD",
                            "code": "USD"
                        }
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702"
                },

                {
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
                }     ]

