
# numbers = [16, 18, 1, 6, 3, 2, 6, 2, 14, 3, 20, 15, 19, 4, 18, 15, 15, 4, 20, 18]
# set1 = set()
# for number in numbers:
#     if number % 3 == 0 or number % 5 == 0:
#         set1.add(number)
# print(set1)
#
# print({number for number in numbers if number % 3 == 0 or number % 5 == 0})


# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 5, "d": 7, "a": 8}
# common_keys = list(dict1.keys() & dict2.keys())
# if common_keys:
#     print("Общие ключи:", common_keys)
# print (list(dict1.keys() & dict2.keys()))

# words = ["apple", "banana", "cherry", "date"]
# print ({key: len(key) for key in words})


# dict1 = {"a": 1, "b": 2}
# dict2 = {"a": 1, "b": 2, "c": 3}
# subset = dict1.items() <= dict2.items()
# print(subset)


# data = {"a": None, "b": 2, "c": "", "d": [], "e": [1, 2]}
# print({key: value for key, value in data.items() if value})


# book = {1: "Начало истории", 2: None, 3: "Глава 1", 4: None, 5: "Глава 2"}
# print("измененый вариант:", {key: ("Страница потеряна" if value is None else value) for key, value in book.items()})


# grades = {
# "anna": [5, 4, 3, 5],
# "bennet": [3, 2, 4],
# "john": [5, 5, 5]
# }
# for key, value in grades.items():
#     grades[key] = {"grade": value, "средний": sum(value)/len(value)}
# print(grades)


# recipes = {
# ("flour", "egg", "milk"): "Pancakes",
# ("egg", "milk", "butter"): "Omelette",
# ("flour", "sugar", "butter"): "Cookies",
# ("flour", "egg", "butter", "sugar"): "Cake",
# ("milk", "flour", "egg"): "Waffles",
# ("butter", "milk", "egg"): "Scrambled Eggs",
# ("flour", "milk", "sugar", "butter"): "Sweet Bread"
# }
# ingredients = "Milk egg butter flour".lower().split()
# found = False
# for key, value in recipes.items():
#     if set(key).issubset(ingredients):
#         found = True
#         print(value)
# if not found:
#     print("Нет рецептов")



# students = {
# "Alice": ["Math", "Physics"],
# "Bob": ["Math", "Physics"],
# "Charlie": ["Chemistry", "Biology"],
# "David": ["Math", "Physics"],
# "Eve": ["Chemistry", "Biology"]
# }
# groups = {}
# for students, subj in students.items():
#     key = frozenset(subj)
#     if key not in groups:
#         groups[key] = []
#     groups[key].append(students)
# print(groups)
# for less, students in groups.items():
#     print("Группа с предметами:", ", ".join(less) + ":", students)


english_words = {
"Butterfly": "Бабочка",
"Training": "Обучение",
"Restaurant": "Ресторан",
"Programming": "Программирование",
}
while True:
    word = input("Enter a word in English (or 'exit' for Exit): ")
    if word.lower() == "exit":
        print("program completed")
        break
    if word in english_words:
        print("Translation:", english_words[word])
    else:
        print("No translation.")
        add = input("Would you like to add a translation? (yes/no): ")
        if add.lower() == "yes":
            translation = input(f'Enter translation "{word}": ')
            english_words[word] = translation
            print(f'Word "{word}" has been added to the dictionary.')
