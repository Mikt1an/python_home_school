"""
Задача 1
Сортировка чисел
Напишите программу, которая запрашивает у пользователя три числа и выводит их в порядке возрастания, разделенные запятой.
Пример вывода:
Введите первое число: 5
Введите второе число: 2
Введите третье число: 7
Числа в порядке возрастания: 2, 5, 7
"""

firstnumber = int(input("Enter first number: "))
secondnumber = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
if firstnumber < secondnumber and firstnumber < number3:
    first = firstnumber
    if secondnumber < number3:
        second = secondnumber
        third = number3
    else:
        second = number3
        third = secondnumber
elif secondnumber < firstnumber and secondnumber < number3:
    first = secondnumber
    if firstnumber < number3:
        second = firstnumber
        third = number3
    else:
        second = number3
        third = firstnumber
else:
    first = number3
    if firstnumber < number3:
        second = firstnumber
        third = number3
    else:
        second = secondnumber
        third = number3
print ("Number 1: ", firstnumber)
print ("Numbers 2: ", secondnumber)
print ("Numbers 3: ", number3)
print ("Numbers in ascending order: ", first, second, third)

"""
Задача 2
Високосный год
Напишите программу, которая запрашивает у пользователя год и проверяет, является ли он високосным. 
Год является високосным, если он делится на 4 без остатка, и в то же время не делится на 100 без остатка. 
При этом если год делятся на 400 без остатка, он тоже является високосным. Выведите соответствующее сообщение на экран 
с помощью функции print.
Пример вывода:
Введите год: 2024
Год является високосным.
Введите год: 2000
Год является високосным.
Введите год: 1900
Год не является високосным.
"""

age = int(input("Введите год: "))
print ("Год является високосным." if age % 4 == 0 and age % 100 != 0 or age % 400 == 0 else "Год не является високосным.")
