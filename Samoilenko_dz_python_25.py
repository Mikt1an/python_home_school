
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
    print("Incorrect number entered.")
except ZeroDivisionError:
    print("Error: Division by zero!")


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
        raise ValueError("Incorrect number entered")

    if divisor == 0:
        raise ZeroDivisionError (f"Incorrect number entered (ZeroDivisionError)")

    return dividend / divisor


try:
    x = float(input("dividend: "))
    b = float(input("divisor: "))
    print(safe_division(x, b))
except ValueError as e:
    print(f"Incorrect number entered: {e}")
    logging.error(f"Incorrect number entered: {e}")
except ZeroDivisionError as e:
    print(f"{e}")
    logging.error(f"{e}")
