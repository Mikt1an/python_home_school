# Задание 1
#     Простое число
# Напишите функцию, которая проверяет, является ли число n простым (делится только на 1 и само себя)
# и возвращает булевый результат.
# Данные:
# n = 17
# Пример вывода:
# Число 17 является простым

n = 17
def prime_number(number : int):
    """
    Checks whether a number is prime.

    A prime number is a natural number greater than 1
    that is divisible only by 1 and itself.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, otherwise False.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
if prime_number(n):
    print(f"Число {n} является простым")
else:
    print(f"Число {n} НЕ является простым")

# Задание 2
#     Фильтрация чисел по чётности
# Напишите функцию, которая принимает filter_type ("even" или "odd") и произвольное количество чисел,
# возвращая только те, которые соответствуют фильтру.
# Пример вызова:
# print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
# print(filter_numbers("odd", 10, 15, 20, 25))
# print(filter_numbers("prime", 2, 3, 5, 7))
# Пример вывода:
# [2, 4, 6]
# [15, 25]
# Некорректный фильтр

def filter_numbers(filter_type: str, *numbers: list):
    """
    Filters numbers by type: even or odd.

    Args:
        filter_type (str): The filter type ("even" or "odd").
        *numbers (int): An arbitrary number of integers.

    Returns:
        list: A list of filtered numbers or an error message.
    """
    if filter_type == "even":
        return [n for n in numbers if n % 2 == 0]
    elif filter_type == "odd":
        return [n for n in numbers if n % 2 != 0]
    return "Некорректный фильтр"
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))



# Задание 3
#     Объединение словарей
# Напишите функцию, которая принимает любое количество словарей и объединяет их в один.
# Если ключи повторяются, используется значение из последнего словаря.
# Данные:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# dict3 = {"d": 5}
# Пример вызова:
# print(merge_dicts(dict1, dict2, dict3))
# Пример вывода:
# {'a': 1, 'b': 3, 'c': 4, 'd': 5}

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

def merge_dicts(*args: dict):
    """
    Merges an arbitrary number of dictionaries into one.
    If keys overlap, the value from the last dictionary is used.

    Args:
        *args (dict): An arbitrary number of dictionaries.

    Returns:
        dict: A new dictionary containing the merged data.
    """
    result = {}
    for dictionary in args:
        result.update(dictionary)
    return result
print(merge_dicts(dict1, dict2, dict3))