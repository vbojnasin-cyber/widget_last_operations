import logging
from pathlib import Path
from src import loggers

name = Path(__file__).stem
file_name = f"{name}.log"
logger = loggers.create_logger(name, file_name, logging.DEBUG)

def get_mask_card_number(number_card: str) -> str:
    """Функция которая маскирует номер карты"""
    if number_card == " " or number_card == "":
        error_msg = f"Номер карты не может быть пустым, вы ввели: '{number_card}'"
        logger.error(error_msg)
        raise ValueError(error_msg)
    clean_number_card = number_card.replace(" ", "")
    if not clean_number_card.isdigit():
        error_msg = f"Номер карты должен состоять только из цифр, вы ввели: '{clean_number_card}'"
        logger.error(error_msg)
        raise ValueError(error_msg)
    if len(clean_number_card) != 16:
        error_msg = f"Номер карты должен содержать 16 цифр, ваш содержит: {len(clean_number_card)}"
        logger.error(error_msg)
        raise ValueError(error_msg)

    logger.info("Номер карты успешно замаскирован")
    return f"**** **** **** {clean_number_card[-4:]}"

def get_mask_account(number_account: str) -> str:
    """Функция, которая маскирует номер счета"""
    if number_account == " " or number_account == "":
        error_msg = f"Номер счета не может быть пустым, вы ввели: '{number_account}'"
        logger.error(error_msg)
        raise ValueError(error_msg)
    clean_number_account = number_account.replace(" ", "")
    if not clean_number_account.isdigit():
        error_msg = f"Номер счета должен состоять только из цифр, вы ввели: '{clean_number_account}'"
        logger.error(error_msg)
        raise ValueError(error_msg)
    if len(clean_number_account) != 20:
        error_msg = f"Номер счета должен состоять из 20 цифр, ваш состоит из {len(clean_number_account)}"
        logger.error(error_msg)
        raise ValueError(error_msg)

    logger.info("Номер счета успешно замаскирован")
    return f"** {clean_number_account[-4:]}"
