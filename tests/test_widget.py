import pytest

from src.widget import mask_account_card

def test_return_mask_account_card():
    assert mask_account_card("Visa Mastercard 1111111111111111") == "Visa Mastercard **** **** **** 1111"
def test_sym_and_num_mask_account_card():
    with pytest.raises(ValueError):
        mask_account_card("Visa Mastercard 112212fgf2231111")
def test_list_mask_account_card():
    with pytest.raises(ValueError):
        mask_account_card(["Visa", "Mastercard", "1233333333333333"])
def test_long_num_mask_account_card():
    with pytest.raises(ValueError):
        mask_account_card("Visa Mastercard 11111111111111111")