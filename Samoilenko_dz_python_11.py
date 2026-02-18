"""
Задание №1
Звёздочки вместо чисел
Напишите программу, которая заменяет все цифры в строке на звёздочки *.
text = "My number is 123-456-789"
Пример вывода:
Строка: My number is 123-456-789
Результат: My number is ***-***-***
"""

text = "My number is 123-456-789"
print("Строка: ", text)

for num in text:
    if num.isdigit():
        text = text.replace(num, "*")
print(text)

"""
Задание №2
Количество символов
Напишите программу, которая подсчитывает количество вхождений всех символов в строке. Нужно вывести только символы, 
которые встречаются более 1 раза (игнорируя регистр), с указанием их количества. 
Выводите повторяющиеся символы только один раз.
text = "Programming in python"
Пример вывода:
Строка: Programming in python
Символ 'p' встречается 2 раз(а)
Символ 'r' встречается 2 раз(а)
Символ 'o' встречается 2 раз(а)
Символ 'g' встречается 2 раз(а)
Символ 'm' встречается 2 раз(а)
Символ 'i' встречается 2 раз(а)
Символ 'n' встречается 3 раз(а)
Символ ' ' встречается 2 раз(а)
"""

text = "Programming in python"
print("Строка:", text)
text= text.lower()
checked = ""
for num in text:
    if num not in checked:
        count = text.count(num)
        if count > 1:
            print(f"Символ '{num}' встречается {count} раз(а)")
        checked += num

"""
Задание №3
Увеличение чисел
Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
Пример вывода:
I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.
"""

text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
text = text.split()
textnew = ""
for elem in text:
    if elem.isdigit():
        textnew += str(float(elem) * 10) + " "
        continue
    elif elem.find(".") != -1:
        spfloat = elem.split(".")
        if spfloat[0].isdigit() and spfloat[1].isdigit():
            textnew += str(float(spfloat[0] + "." + spfloat[1]) * 10) + " "
        else:
            textnew += elem + " "
    else:
        textnew += elem + " "
print(textnew)