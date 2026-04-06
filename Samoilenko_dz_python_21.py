# Задание 1
#     Повторения букв
# Реализуйте функцию, которая принимает текст и возвращает словарь с подсчётом количества каждой буквы,
# игнорируя регистр.
# Данные:
# text = "Programming is fun!"
# Пример вывода:
# {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}

text = "Programming is fun!"
print("V1")
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


print("V2")
from collections import Counter

def count_letters(texte : str) -> dict[str, int]:
    """
    Count occurrences of each letter in a given text, ignoring case.

    This function processes the input string, filters out all non-alphabetic
    characters, converts remaining letters to lowercase, and returns a dictionary
    with the frequency of each letter.

    Args:
        texte : str The input string to analyze.
    Returns:
        dict : A dictionary where keys are lowercase letters and values are their counts.
    Raises:
        TypeError : If the input is not a string.
    """
    if not isinstance(texte, str):
        raise TypeError("Аргумент должен быть строкой")


    filtered = [char.lower() for char in texte if char.isalpha()]

    return dict(Counter(filtered))


result = count_letters(text)
print(result)

# Задание 2
#     Группировка студентов по классам
# Создайте структуру для группировки студентов по классам.
# Добавьте студентов в соответствующие группы.
# Данные:
# students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
# Пример вывода:
# {'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

print("V1")
def group_students(studentss: list[tuple[str, str]]):
    """
    Groups students by their classes.

    Args:
        studentss (list[tuple[str, str]]): A list of tuples where each tuple
            contains (class_name, student_name).

    Returns:
        dict[str, list[str]]: A dictionary where keys are class names and
            values are lists of student names.
    """
    result = {}
    for class_name, student_names in studentss:
        if class_name not in result:
            result[class_name] = []
        result[class_name].append(student_names)
    return result

print(group_students(students))


print("V2")
from collections import defaultdict

def students_group(studentss : list[tuple[str, str]]) -> dict[str, list[str]]:
    """
    Group students by their class.

    This function takes a list of (class, student_name) tuples and
    organizes them into a dictionary where each class maps to a list
    of students belonging to that class.

    Args:
        students : list[tuple[str, str]] A list of tuples where each tuple contains a class name and a student name.
    Returns:
        dict[str, list[str]] A dictionary where keys are class names and values are lists of student names.
    Raises:
        TypeError If input is not a list or contains invalid elements.
    """

    if not isinstance(studentss, list):
        raise TypeError("Input must be a list")

    grouped = defaultdict(list)

    for item in studentss:
        if not isinstance(item, tuple) or len(item) != 2:
            raise TypeError("Each item must be a tuple of (class, student_name)")

        class_name, student_name = item
        grouped[class_name].append(student_name)

    return dict(grouped)


print(students_group(students))