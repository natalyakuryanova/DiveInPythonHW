# -*- coding: utf8 -*-
from datetime import datetime, timedelta

def get_new_date(d):
    """
    Возвращает дату, которая наступит через указанное количество дней от текущей даты.
    :param d: Количество дней от текущей даты.
    :return: Отформатированная дата в формате YYYY-MM-DD.

    Примеры:
    >>> get_new_date(30)
    '2024-10-23'
    >>> get_new_date(-10)
    '2024-09-13'
    """

    # Получить текущее время и дату
    now = datetime.now()

    # Вычисление даты через указанное количество дней
    new_date = now + timedelta(days=d)

    # Форматирование будущей даты в строку в формате YYYY-MM-DD
    formatted_new_date = new_date.strftime('%Y-%m-%d')

    return formatted_new_date


if __name__ == '__main__':
    days = -10  # Количество дней для вычисления
    print(f'Date {days} days from now: {get_new_date(days)}')
