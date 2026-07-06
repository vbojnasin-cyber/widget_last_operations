from unittest.mock import patch
import pytest

from src.widget import mask_account_card

# Test for the func mask_account_card

# 1 test
def test_mask_account_card_visa():
    """Тест корректной обработки карты Visa."""
    with patch("src.widget.get_mask_card_number", return_value="**** **** **** 4567") as mock_card:
        result = mask_account_card("Visa Platinum 1234567812344567")

        assert result == "Visa Platinum **** **** **** 4567"
        mock_card.assert_called_once_with("1234567812344567")

# 2 test
def test_mask_account_card_account():
    """Тест корректной обработки счета."""
    with patch("src.widget.get_mask_account", return_value="** 4321") as mock_account:
        result = mask_account_card("Счет 73443456789012344321")

        assert result == "Счет ** 4321"
        mock_account.assert_called_once_with("73443456789012344321")


# 3 test
def test_mask_account_card_bubbles_up_exception():
    """Тест перехвата и перевызова ошибок из функций маскирования."""
    # И здесь тоже меняем путь для патча
    with patch("src.widget.get_mask_card_number", side_effect=ValueError("неверная длина")):
        with pytest.raises(ValueError) as exc_info:
            mask_account_card("Visa 123")

        assert "Ошибка маскирования" in str(exc_info.value)
        assert "неверная длина" in str(exc_info.value)
