from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_account: str) -> str:
    """Функция возврщает строку с замаскированным номером"""
    if not isinstance(number_account, str):
        raise ValueError(
            f"Данные должны быть строкой, ваш тип данных - {type(number_account)}"
        )
    if not number_account:
        raise ValueError(f"Строка не может быть пуста, вы ввели - {number_account}")
    parts = number_account.split()
    number_card = parts[-1]
    type_card = " ".join(parts[:-1])
    if not number_card.isdigit():
        raise ValueError(
            f"Номер карты должен состоять только из цифр, ваш номер карты - {number_card}"
        )
    try:
        if type_card.lower().startswith("счет"):
            mask_card = get_mask_account(number_card)
        else:
            mask_card = get_mask_card_number(number_card)
        return f"{type_card} {mask_card}".strip()
    except ValueError as e:
        raise ValueError(f"Ошибка маскирования {e}")
