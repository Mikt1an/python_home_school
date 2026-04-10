# Задача 1
# Деление без ошибок
# Напишите функцию, которая выполняет деление двух чисел, введенных пользователем, и обрабатывает возможные ошибки.
# Пример вывода:
# Введите делимое: 345
# Введите делитель: 5a
# Ошибка: Введено некорректное число.


def func_division(dividend : float, divisor : float) -> float :
    """
    Divides two numbers using a custom error handler.

    This is a higher-order function: it takes another function (handler)
    to process exceptions (e.g., division by zero).

    Args:
        dividend (float): The dividend value to divide.
        divisor (float): The divisor value to divide.
    Returns:
        float: The result of the division.
    """
    return dividend / divisor


try:
    x = float(input("dividend: "))
    b = float(input("divisor: "))
    print(func_division(x, b))
except ValueError:
    print("Введено некорректное число.")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")


# Задача 2
# Логирование ошибок
# Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log в соответствии с форматом ниже.
# Пример вывода:
# 2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число

import logging

logging.basicConfig(
        filename="errors.log",
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s",
        encoding="utf-8"
    )


def safe_division(dividend : float, divisor : float) -> float :
    """
    Divides two numbers using a custom error handler.

    This is a higher-order function: it takes another function (handler)
    to process exceptions (e.g., division by zero).

    Args:
        dividend (float): The dividend value to divide.
        divisor (float): The divisor value to divide.
    Returns:
        float: The result of the division.
    """

    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise ValueError("Ошибка: Введено некорректное число")

    if divisor == 0:
        raise ZeroDivisionError (f"Ошибка: Введено некорректное число (ZeroDivisionError)")

    return dividend / divisor


try:
    x = float(input("dividend: "))
    b = float(input("divisor: "))
    print(safe_division(x, b))
except ValueError as e:
    print(f"Ошибка: Введено некорректное число:")
    logging.error(f"Ошибка: Введено некорректное число:")
except ZeroDivisionError as e:
    print(f"{e}")
    logging.error(f"{e}")
