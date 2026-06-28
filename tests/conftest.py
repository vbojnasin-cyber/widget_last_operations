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
