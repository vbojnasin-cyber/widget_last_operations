import pytest
from src.masks import get_mask_card_number


def test_returns_get_mask_card_number(test_name):
    return test_name

def test_valid_get_mask_card_number(test_name):
    assert get_mask_card_number(test_name) == "** 1111"


def test_str_null_get_mask_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number(" ")


def test_invalid_small_number_get_mask_card_number(test_small_number_card):
    with pytest.raises(ValueError):
        get_mask_card_number(test_small_number_card)


def test_sym_and_num_get_mask_card_number(test_num_and_sym_number_card):
    with pytest.raises(ValueError):
        get_mask_card_number(test_num_and_sym_number_card)