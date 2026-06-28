import pytest
from src.masks import get_mask_card_number

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

# test for the get_mask_account func