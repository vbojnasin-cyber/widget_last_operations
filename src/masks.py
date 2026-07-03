def get_mask_card_number(number_card: str) -> str:
    """Функция которая маскирует номер карты"""
    if number_card == " " or number_card == "":
        raise ValueError(
            f"Номер карты не может состоять из пустой строки, вы ввели - {number_card}"
        )
    clean_number_card = number_card.replace(" ", "")
    if not clean_number_card.isdigit():
        raise ValueError(
            f"Номер карты должен состоять только из цифр, номер который вы ввели - {clean_number_card}"
        )
    if len(clean_number_card) != 16:
        raise ValueError(
            f"Номер карты должен содержать 16 цифр, ваш содержит - {len(clean_number_card)}"
        )
    return f"**** **** **** {clean_number_card[-4:]}"


def get_mask_account(number_account: str) -> str:
    """Функция, которая маскирует номер счета"""
    if number_account == " " or number_account == "":
        raise ValueError(
            f"Номер счета не может состоять из пустой строки, вы ввели - {number_account}"
        )
    clean_number_account = number_account.replace(" ", "")
    if not clean_number_account.isdigit():
        raise ValueError(
            f"Номер счета должен состоять только из цифр, номер который вы ввели - {clean_number_account}"
        )
    if len(clean_number_account) != 20:
        raise ValueError(f"Номер счета должен состоять из 20 цифр, ваш состоит из {len(clean_number_account)}")
    return f"** {clean_number_account[-4:]}"
