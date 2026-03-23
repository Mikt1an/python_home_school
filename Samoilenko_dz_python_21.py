# Задание 1
#     Повторения букв
# Реализуйте функцию, которая принимает текст и возвращает словарь с подсчётом количества каждой буквы,
# игнорируя регистр.
# Данные:
# text = "Programming is fun!"
# Пример вывода:
# {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}

text = "Programming is fun!"

def letter_counter(full_text : str):
    """
    Takes a string, converts it to lowercase,
    and returns a dictionary where keys are letters
    and values are their occurrence counts.

    Args:
        full_text (str): Input string to analyze.
    Returns:
        dict: A dictionary where keys are letters and values are their counts.
    """
    result = {}
    for letter in full_text:
        if letter not in result and letter.isalpha():
            result[letter.lower()] = full_text.count(letter)
    return result

print(letter_counter(text))

# Задание 2
#     Группировка студентов по классам
# Создайте структуру для группировки студентов по классам.
# Добавьте студентов в соответствующие группы.
# Данные:
# students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
# Пример вывода:
# {'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

def group_students(students: list[tuple[str, str]]):
    """
    Groups students by their classes.

    Args:
        students (list[tuple[str, str]]): A list of tuples where each tuple
            contains (class_name, student_name).

    Returns:
        dict[str, list[str]]: A dictionary where keys are class names and
            values are lists of student names.
    """
    result = {}
    for class_name, student_names in students:
        if class_name not in result:
            result[class_name] = []
        result[class_name].append(student_names)
    return result

print(group_students(students))