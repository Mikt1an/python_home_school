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
for symbol in text_list[:]:
    if symbol.find(" ") != -1:
        text_list.remove(symbol)
    else:
        index = text_list.index(symbol)
        text_list[index] = symbol.lower()
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
rabat = int(input("Введите скидку (в процентах): ")) / 100
print(f"{"Name":<10}", f"{"Old Price":>11}", f"{"New Price":>15}")
for product in products:
    new_price = product[1] - (product[1] * rabat)
    index = products.index(product)
    products[index] = [product[0], product[1], new_price]
for name, old_price, new_price in products:
    print(f'{name:<10}{old_price:>11.2f}${new_price:>15.2f}$')
