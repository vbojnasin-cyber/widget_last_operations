import pytest

from src.masks import get_mask_account, get_mask_card_number

# Test for the get_mask_card_number func

# 1 test
def test_get_mask_card_number():
    """Тест успешной маскировки корректного номера карты с пробелами и без"""
    assert get_mask_card_number("3123453453424556") == "**** **** **** 4556"
    assert get_mask_card_number("3123 4534 5342 4556") == "**** **** **** 4556"


# 2 test
@pytest.mark.parametrize("empty_input", ["", " "])
def test_get_mask_card_number_empty(empty_input):
    """Тест генерации ошибки при пустой строке или строке из одного пробела."""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(empty_input)
    assert "Номер карты не может быть пустым" in str(exc_info.value)

# 3 test
@pytest.mark.parametrize("invalid_chars", ["1234-5678-1234-5678", "123456781234abcd", "1234 5678 1234 567a"])
def test_get_mask_card_number_not_digit(invalid_chars):
    """Тест генерации ошибки, если в номере есть нецифровые символы."""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(invalid_chars)
    assert "Номер карты должен состоять только из цифр" in str(exc_info.value)

# 4 test
@pytest.mark.parametrize("wrong_length", ["12345", "123456781234567", "12345678123456789"])
def test_get_mask_card_number_wrong_length(wrong_length):
    """Тест генерации ошибки при неверной длине номера (не 16 цифр)."""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(wrong_length)
    assert "Номер карты должен содержать 16 цифр" in str(exc_info.value)


# Test for the get_mask_account func


# 1 test
def test_get_mask_account_success():
    """Тест успешного маскирования корректного номера счета."""
    # 20 цифр с пробелами
    assert get_mask_account("7344 3456 7890 1234 5678") == "** 5678"
    # 20 цифр без пробелов
    assert get_mask_account("73443456789012345678") == "** 5678"

# 2 test
@pytest.mark.parametrize("empty_input", ["", " "])
def test_get_mask_account_empty(empty_input):
    """Тест генерации ошибки при пустой строке или строке из одного пробела."""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(empty_input)
    assert "Номер счета не может быть пустым" in str(exc_info.value)

# 3 test
@pytest.mark.parametrize("invalid_chars", ["7344-3456-7890-1234-5678", "7344345678901234567a"])
def test_get_mask_account_not_digit(invalid_chars):
    """Тест генерации ошибки, если в номере счета есть нецифровые символы."""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(invalid_chars)
    assert "Номер счета должен состоять только из цифр" in str(exc_info.value)


# 4 test
@pytest.mark.parametrize("wrong_length", ["12345", "7344345678901234567", "734434567890123456789"])
def test_get_mask_account_wrong_length(wrong_length):
    """Тест генерации ошибки при неверной длине счета (не 20 цифр)."""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(wrong_length)
    assert "Номер счета должен состоять из 20 цифр" in str(exc_info.value)
