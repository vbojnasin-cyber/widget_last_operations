import pytest

from src.masks import get_mask_account, get_mask_card_number

# Test for the get_mask_card_number func

# 1 test
def test_valid_get_mask_card_number(test_name):
    """Тест с валидными данными"""
    assert get_mask_card_number(test_name) == "**** **** **** 1111"

# 2 test
def test_space_null_get_mask_card_number():
    """Тест обработки ошибки, если пользователь вводит пробел"""
    with pytest.raises(ValueError):
        get_mask_card_number(" ")
# 3 test
def test_str_null_get_mask_card_number():
    """Тест обработки ошибки, если пользователь вводит пустую строку"""
    with pytest.raises(ValueError):
        get_mask_card_number("")

# 4 test
def test_invalid_small_number_get_mask_card_number(test_small_number_card):
    """Тест обработки ошибки, если пользователь вводит короткий номер карты"""
    with pytest.raises(ValueError):
        get_mask_card_number(test_small_number_card)

# 5 test
def test_sym_and_num_get_mask_card_number(test_num_and_sym_number_card,):
    """Тест обработки ошибки, если пользователь вводит номер с цифрами и буквами"""
    with pytest.raises(ValueError):
        get_mask_card_number(test_num_and_sym_number_card)

# 6 test
def test_long_num_get_mask_card_number(test_long_number_card):
    """Тест обработки ошибки, если пользователь вводит слишкои длинный номер карты"""
    with pytest.raises(ValueError):
        get_mask_card_number(test_long_number_card)

# 7 test
def test_space_get_mask_card_number():
    """Тест, если пользователь введет валидный номер карты
     состоящий из 16 чисел, но будут пробелы"""
    assert get_mask_card_number("   1234 3456   6543 6543     ") == "**** **** **** 6543"



# Test for the get_mask_account func

# 1 test
def test_returns_get_mask_account():
    """Тест с валидными данными"""
    assert get_mask_account("22222222222222222222") == "** 2222"

# 2 test
def test_spase_str_get_mask_account():
    """Тест на обработку ошибки, если пользователь вместо номера введет пробел"""
    with pytest.raises(ValueError):
        get_mask_account(" ")

# 3 test
def test_str_null_get_mask_account():
    """Тест на обработку ошибки, если пользователь введет пустую строку"""
    with pytest.raises(ValueError):
        get_mask_account("")

# 4 test
def test_num_and_sym_get_mask_account():
    """Тест на обработку ошибки, если пользователь введет номер счета, который содержит буквы"""
    with pytest.raises(ValueError):
        get_mask_account("2222ffff222222222222")

# 5 test
def test_long_num_get_mask_account():
    """Тест на обработку ошибки, если пользователь ведет номер счета больше чем 20 цифр"""
    with pytest.raises(ValueError):
        get_mask_account("22222222222222222222222222222222222")
