import os
from unittest.mock import patch, MagicMock
from src.external_api import currency_exchange
from dotenv import load_dotenv
import requests
import pytest
load_dotenv()
API_KEY = os.getenv("API_KEY_EXCHANGE")

@patch("src.external_api.requests.get")
def test_currency_exchange_success(mock_get):
    """Тестируем успешный ответ от API"""
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": 7500.0}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    result = currency_exchange(100, "USD")
    assert result == 7500.0
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100",
        headers={"apikey": API_KEY}
    )


@patch("src.external_api.requests.get")
def test_currency_exchange_network_error(mock_get):
    """Тестируем, что функция корректно прокидывает ошибку, если API лежит"""
    mock_get.side_effect = requests.RequestException("Ошибка сети")
    with pytest.raises(requests.RequestException):
        currency_exchange(100, "USD")