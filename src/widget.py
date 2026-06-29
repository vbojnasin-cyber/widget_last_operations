from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(number_account: str) -> str:
    """Функция возврщает строку с замаскированным номером"""
    if not isinstance(number_account, str):
        raise ValueError("Данные должны быть строкой")
    if not number_account:
        raise ValueError("Строка не может быть пуста")
    parts = number_account.split()
    number_card = parts[-1]
    type_card = " ".join(parts[:-1])
    if not number_card.isdigit():
        raise ValueError("Номер карты должен состоять только из цифр")
    try:
        if type_card.lower().startswith("счет"):
            mask_card = get_mask_account(number_card)
        else:
            mask_card = get_mask_card_number(number_card)
        return f"{type_card} {mask_card}".strip()
    except ValueError as e:
        raise ValueError(f"Ошибка маскирования {e}")

