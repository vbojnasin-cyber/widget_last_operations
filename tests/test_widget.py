import pytest

from src.widget import mask_account_card

# Test for the func mask_account_card


# 1 test
def test_valid_number_mask_account_card():
    """Тест при валидных данных банковской карты"""
    assert (
        mask_account_card("Visa Mastercard 1111111111111111")
        == "Visa Mastercard **** **** **** 1111"
    )


# 2 test
def test_valid_account_mask_account_card():
    """Тест при валидных данных счета"""
    assert mask_account_card("Счет 01111111111111111111") == "Счет ** 1111"


# 3 test
def test_letter_in_number_mask_account_card():
    """Тест ошибки, если пользователь введет некорректный номер карты с буквами"""
    with pytest.raises(ValueError):
        mask_account_card("Visa Mastercard 112212fgf2231111")


# 4 test
def test_letter_in_account_mask_account_card():
    """Тест ошибки, если пользователь введет некорректный номер счета с буквами"""
    with pytest.raises(ValueError):
        mask_account_card("Счет 011111ggggggggg11111")


# 5 test
def test_list_mask_account_card():
    """Тест ошибки, если в аргумент передадут список"""
    with pytest.raises(ValueError):
        mask_account_card(["Visa", "Mastercard", "1233333333333333"])


# 6 test
def test_long_number_mask_account_card():
    """Тест при длинном номере карты"""
    with pytest.raises(ValueError):
        mask_account_card("Visa Mastercard 11111111111111111")
