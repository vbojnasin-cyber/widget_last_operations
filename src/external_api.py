import os
import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY_EXCHANGE")


def currency_exchange(amount: float, from_currency: str):
    """Конвертирует указанную сумму иной валюты в рубли"""
    if not API_KEY:
        raise ValueError("API_KEY не найден в окружениях")
    to_currency = "RUB"
    from_currency = from_currency.upper()
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

    headers = {"apikey": API_KEY}

    try:

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        if "result" in data:
            return float(data["result"])
        else:
            raise KeyError("Не удалось конвертировать валюту")
    except requests.RequestException as e:
        print(f"Ошибка к подключению API")
        raise


if __name__ == "__main__":
    print(currency_exchange(100, "USD"))