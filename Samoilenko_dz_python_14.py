"""
Задание №1
Число в конце
Напишите программу, которая создает новый список. В него необходимо добавить только те строки из исходного списка,
в которых цифры находятся только в конце.
Данные:
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
Пример вывода:
Строки с цифрами только в конце: ['apple23', 'grape3']
"""

strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
new_strings = []
for string in strings:
    for numb in range(len(string)-1, -1, -1):
        if string[numb].isdigit():
            continue
        else:
            if string[:numb+1].isalpha():
                new_strings.append(string)
            else:
                break
        break
print(new_strings)

"""
Задание №2
Удаление кратных
Напишите программу, которая удаляет из списка все значения, кратные числу, которое вводится пользователем.
Данные:
numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
Пример вывода:
Введите число для удаления кратных ему элементов: 3
Список без кратных значений: [1, 10, 19, 20]
"""

numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
user_input = int(input("Введите число для удаления кратных ему элементов: "))
remove_list = []
for number in numbers:
    if number%user_input == 0:
        remove_list.append(number)
for index in remove_list:
    numbers.remove(index)
print("Список без кратных значений: ", numbers)

"""
Задание №3
Порядок четных
Напишите программу, которая формирует новый список чисел. Добавьте в него все элементы исходного списка, где:
    нечетные числа занимают те же позиции,
    чётные числа отсортированы между собой обратном порядке.
Данные:
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
Пример вывода:
Список после сортировки: [5, 8, 3, 4, 2, 1, 2, 7]
"""

numbers = [5, 2, 3, 8, 4, 1, 2, 7]
print(numbers)
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
evens.sort(reverse=True)
result = []
i = 0
for n in numbers:
    if n % 2 != 0:
        result.append(n)
    else:
        result.append(evens[i])
        i += 1
print("Список после сортировки:", result)