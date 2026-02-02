"""
Задание 1
Сумма цифр числа
Напишите программу, которая получит четырехзначное число от пользователя и выведет на экран сумму цифр этого числа.
Пример вывода:
Введите четырехзначное число: 1634
Сумма цифр числа: 14
"""

numbers = input("Please enter a four-digit number: ")
sumnumbers = int(numbers[0]) + int(numbers[1]) + int(numbers[2]) + int(numbers[3])
print(f"Sum of the digits of the number: {sumnumbers}")

"""
Задание 2
Напишите программу, которая получает два числа от пользователя, умножает одно число на второе и выводит результат и оба 
числа через дефис. Не сохраняете результат умножения в переменной.
Пример вывода:
Введите первое число: 4
Введите второе число: 5
Результат: 20-4-5
"""

firstnumber = int(input("Please enter the first number: "))
secondnumber = int(input("Please enter the second number: "))
print ("Result", end=': ')
print (firstnumber * secondnumber, firstnumber, secondnumber, sep='-')

"""
Задание 3 - Вычисление без операторов % и //
Напишите программу, которая получает два числа от пользователя и вычисляет:
- Остаток от деления
- Результат целочисленного деления

Решить без использования операторов % и //.

Пример ввода:
Введите первое число: 10  
Введите второе число: 3
Пример вывода:
Остаток от деления: 1  
Целочисленное деление: 3
"""


firstnumber2 = int(input("Please enter the first number: "))
secondnumber2 = int(input("Please enter the second number: "))
integerdiv = int(firstnumber2 / secondnumber2)
remainderdiv = firstnumber2 - (secondnumber2 * integerdiv)
print (f"Remainder of the division: {remainderdiv}\nInteger division result: {integerdiv}")