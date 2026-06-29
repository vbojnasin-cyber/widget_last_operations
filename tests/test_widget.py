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
@pytest.mark.parametrize(
    "number_card, expected",
    [
        (
            "Maestro 1596837868705199",
            "Maestro **** **** **** 5199"
        ),
        (
            "Счет 64686473678894779589",
            "Счет ** 9589"
        )
])
def test_mask(number_card, expected):
    assert mask_account_card(number_card) == expected