# 1. Сумма цифр числа
# Напишите рекурсивную функцию, которая находит сумму всех цифр числа.
# Данные:
# num = 43197
# Пример вывода:
# 24

num = 43197


def sum_numbers(nums: int) -> int:
    """
    Sums all the numbers up to and including nums.

    Args:
        nums: A list containing elements of any type.
    Returns:
        sum all the numbers up to and including nums.
    """
    if nums <= 0:
        return nums
    return nums % 10 + sum_numbers(nums // 10)


print(sum_numbers(num))


# 2. Сумма вложенных чисел
# Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.
# Данные:
# nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
# Пример вывода:
# 28

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]


def sum_list(nums: list) -> int:
    """
    Recursively calculates the sum of all integers in a nested list.

    The function iterates through each element of the list:
    - If the element is an integer, it is added to the total sum.
    - If the element is a list, the function calls itself recursively
      to sum the elements inside that list.

    Args:
        nums: A list containing integers or nested lists of integers.

    Returns:
        The total sum of all integers found in the nested structure.
    """
    return sum(value if isinstance(value, int) else sum_list(value) for value in nums )


print(sum_list(nested_numbers))