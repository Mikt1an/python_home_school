# Задание 1
#     Реверс словаря
# Напишите программу, которая меняет местами ключи и значения в словаре.
# Если значения повторяются, добавьте их в список.
# Данные:
# data = {"a": 1, "b": 2, "c": 1, "d": 3}
# Пример вывода:
# Перевернутый словарь: {1: ['a', 'c'], 2: ['b'], 3: ['d']}

data = {"a": 1, "b": 2, "c": 1, "d": 3}
revers_data = {}
for key, item in data.items():
    if item not in revers_data:
        revers_data[item] = [key]
    else:
        revers_data[item].append(key)
print("Перевернутый словарь:", revers_data)

# Задание 2
#     Счётчик букв в словах
# Напишите программу, которая подсчитывает количество каждой буквы в заданных словах и создаёт словарь,
# где ключи — это слова, а значения — это ещё один словарь с подсчётом каждой буквы.
# Данные:
# words = ["anna", "bennet", "john"]
# Пример вывода:
# {'anna': {'a': 2, 'n': 2}, 'bennet': {'b': 1, 'e': 2, 'n': 2, 't': 1}, 'john': {'j': 1, 'o': 1, 'h': 1, 'n': 1}}


words = ["anna", "bennet", "john"]
result =  {}
for word in words:
    let = {}
    for letter in set(word):
        let[letter] = word.count(letter)
    result[word] = let
print(result)

# Задание 3
#     Распределение студентов по группам
# У вас есть словарь, где ключи — имена студентов, а значения — их баллы за экзамен.
# Необходимо распределить студентов по группам:
#     "Отличники": баллы >= 85
#     "Хорошисты": баллы от 70 до 84
#     "Троечники": баллы от 50 до 69
#     "Не сдали": баллы < 50
# Создайте словарь с ключами-группами и словарями со студентами в качестве значений.
# Данные:
# students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
# groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]
# Пример вывода:
# Распределение по группам:
# {'Отличники': {'Аня': 92, 'Дима': 88}, 'Хорошисты': {'Боря': 76},
# 'Троечники': {'Ваня': 65, 'Ева': 54}, 'Не сдали': {'Галя': 48}}

print("V1")
students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]
gro = {}
for group in groups:
    sum_group = {}
    for student in students.keys():
        if students[student] >= 85 and group == "Отличники":
            sum_group[student] = students[student]
        elif 84 >= students[student] >= 70 and group == "Хорошисты":
            sum_group[student] = students[student]
        elif 69 >= students[student] >= 50 and group == "Троечники":
            sum_group[student] = students[student]
        elif students[student] < 50 and group == "Не сдали":
            sum_group[student] = students[student]
    gro[group] = sum_group
print(gro)

print("V2")
gro = {group: {} for group in groups}
for student in students:
    score = students[student]
    if score >= 85:
        gro["Отличники"][student] = score
    elif score >= 70:
        gro["Хорошисты"][student] = score
    elif score >= 50:
        gro["Троечники"][student] = score
    else:
        gro["Не сдали"][student] = score
print(gro)
