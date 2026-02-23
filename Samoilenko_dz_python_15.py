"""
Задача№1
Одно слово
Напишите программу, которая обрабатывает список из строк и удаляет все строки, содержащие более одного слова,
а также преобразует оставшиеся строки к нижнему регистру.
Данные:
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
Пример вывода:
Обработанный список: ['hello', 'world', 'simple']
"""

text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
print(text_list)
index = 0
rem = []
for t_list in text_list:
    t_list = t_list.lower()
    text_list[index] = t_list
    if t_list.find(" ") != -1:
        rem.append(t_list)
    index += 1
for remo in rem:
    text_list.remove(remo)
print(text_list)

"""
Задача№2
Обновление цен товаров
Дан список товаров с ценами. Программа должна применить скидку к каждому товару и добавить в список элемент с новой ценой. 
В конце вывести таблицу с новой ценой.
Данные:
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
Пример вывода:
Введите скидку (в процентах): 17
Товар          Старая цена    Новая цена
Laptop            1200.00$       996.00$
Mouse                25.00$         20.75$
Keyboard           75.00$         62.25$
Monitor            200.00$       166.00$
"""

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
rabat = int(input("Введите скидку (в процентах): "))
rabat = rabat / 100
print(rabat)
print(f"{"Name":<10}", f"{"Old Price":>11}", f"{"New Price":>15}")
for name, price in products:
    print(f"{name:<10}", f"{price:>10.2f}$", f"{price - (price*rabat):>14.2f}$")