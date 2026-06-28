import pytest
from src.masks import get_mask_card_number, get_mask_account

# Test for the get_mask_card_number func
def test_returns_get_mask_card_number(test_name): # Тест чтобы понять, что возвращает функция
    return test_name

def test_valid_get_mask_card_number(test_name): # Тест с валидными данными
    assert get_mask_card_number(test_name) == "** 1111"

def test_str_null_get_mask_card_number(): # Тест обработки ошибки, если пользователь вводит пробел или пустую строку
    with pytest.raises(ValueError):
        get_mask_card_number(" ")

def test_invalid_small_number_get_mask_card_number(test_small_number_card): # Тест обработки ошибки, если пользователь вводит короткий номер карты
    with pytest.raises(ValueError):
        get_mask_card_number(test_small_number_card)

def test_sym_and_num_get_mask_card_number(test_num_and_sym_number_card): # Тест обработки ошибки, если пользователь вводит номер с цифрами и буквами
    with pytest.raises(ValueError):
        get_mask_card_number(test_num_and_sym_number_card)

# Test for the get_mask_account func
def test_returns_get_mask_account():
    assert get_mask_account("22222222222222222222") == "** 2222" # Тест на return

def test_spasec_str_get_mask_account(): # Тест на обработку ошибки, если пользователь вместо номера введет пустую строку
    with pytest.raises(ValueError):
        get_mask_account(" ")
def test_num_and_sym_get_mask_account(): # Тест на обработку ошибки, если пользователь введет номер счета с символами
    with pytest.raises(ValueError):
        get_mask_account("2222ffff222222222222")
def test_long_num_get_mask_account(): # Тест на обработку ошибки, если пользователь ведет номер счета длинее чем 20 цифр
    with pytest.raises(ValueError):
        get_mask_account("22222222222222222222222222222222222")