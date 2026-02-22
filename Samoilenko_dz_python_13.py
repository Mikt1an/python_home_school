"""
Задание №1
Прогрессия увеличения
Напишите программу, которая создаёт новый кортеж, состоящий из элементов изначального в том же порядке.
Добавить в него только элементы, которые больше всех предыдущих значений в исходном кортеже.
Данные:
numbers = (3, 7, 2, 8, 5, 10, 1)
Пример вывода:
Кортеж по возрастанию: (3, 7, 8, 10)
"""

numbers = (3, 7, 2, 8, 5, 10, 1)
print(numbers)
print(type(numbers))
newnumbers = []
maxnumb = numbers[0]
for numb in numbers:
    if numb >= maxnumb:
        newnumbers.append(numb)
        maxnumb = numb
my_tuple = tuple(newnumbers)
print(my_tuple)
print(type(my_tuple))

"""
Задание №2
Повторяющиеся элементы
Напишите программу, которая находит индексы элементов кортежа, встречающихся более одного раза. 
Вывести сами элементы и их индексы.
Данные:
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
Пример вывода:
Индексы элемента 2: 1 4 9 
Индексы элемента 3: 2 6 
Индексы элемента 4: 3 8
"""

numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
print(numbers)
indexmax = {}
for index, number in enumerate(numbers):
    if number not in indexmax:
        indexmax[number] = []
    indexmax[number].append(index)
for index, value in indexmax.items():
    if len(value) > 1:
        print(f"Индексы элемента {index}: ", *value)
