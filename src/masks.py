
def get_mask_card_number(number_card: str) -> str:
    """Функция которая накладывает маску на номер карты"""
    if number_card == " " and number_card == "":
        raise ValueError("Номер карты не может состоять из пустой строки")
    clean_number_card = number_card.replace(" ", "") #Убираем пробелы
    if not clean_number_card.isdigit():
        raise ValueError(f"Номер карты должен состоять только из цифр")
    if len(clean_number_card) != 16: #Проверяем на валидность номер карты
        raise ValueError(
            f"Номер карты должен содержать 16 цифр,"
            f" ваш содержит - {len(clean_number_card)}") #Обрабатываем ошибку


    return f"** {clean_number_card[-4:]}"  #Вывод номера карты с маской