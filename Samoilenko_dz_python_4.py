"""
Задача 1
Логические операции
Напишите программу, которая получит два логических значения от пользователя и выведет результат логических операций and,
or, not для этих значений, а также сравнение на равенство и неравенство. Для операции not используйте первое число.
Продумайте в каком виде получать ввод от пользователя для логического значения.
Пример вывода:
Enter first value: <value1>
Enter second value: <value1>
and: True
or: True
not: False
equal: False
not equal: True
"""

value1 = int(input("Enter first value: "))
value2 = int(input("Enter second value: "))
print("and: ", bool(value1) and bool(value2))
print("or: ", bool(value1) or bool(value2))
print("not: ", not value1)
print("equal: ", value1 == value2)
print("not equal: ", value1 != value2)

"""
Задача 2
Проверка условий
Напишите программу, которая принимает на вход логические значения двух переменных (свет включён и окно открыто) и проверяет:
    Оба ли условия выполнены.
    Хотя бы одно из условий выполнено.
Пример вывода:
Свет включён? True  
Окно открыто? False  
Оба условия выполнены? False  
Хотя бы одно условие выполнено? True
"""

light_input = input("Is the light on? (True/False): ")
window_input = input("Is the window open? (True/False): ")
print ("Is the light on? ", light_input == "True")
print ("Is the window open? ", window_input == "True")
print ("Are both conditions met? ", light_input == "True" and window_input == "True")
print ("Is at least one condition met? ", light_input != window_input)

"""
Задача 3
Стоимость мобильного тарифа
Напишите программу для расчёта стоимости использования мобильного тарифа:
    Базовая стоимость: 30 евро.
    Каждый мегабайт интернета сверх 500 МБ стоит 0.2 евро.
Программа должна запросить у пользователя количество использованных мегабайтов и вывести сколько всего он заплатил (базовый и переплата).
Пример вывода:
Введите использованные мегабайты: 510
Общая стоимость: 32.0
"""

tariff = 30
usemb = int(input("Please enter the used megabytes: "))
print("used megabytes: ", usemb)
print("tariff 500MB = ", tariff)
if usemb <= 500:
    print ("The used megabytes is less than 500 MB = 30 euro")
else:
    overtariff = (usemb - 500) * 0.2
    print ("The used megabytes is over than 500 MB = ", tariff + overtariff, "euro")



