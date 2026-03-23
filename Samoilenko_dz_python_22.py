# Задание 1
# Выбор заказов
# У вас есть список заказов. Каждый заказ содержит название продукта и его цену.
# Напишите функцию, которая:
#     Отбирает заказы дороже 500.
#     Создаёт список названий отобранных продуктов в алфавитном порядке.
#     Возвращает итоговый список названий.
# Данные:
# orders = [
#     {"product": "Laptop", "price": 1200},
#     {"product": "Mouse", "price": 50},
#     {"product": "Keyboard", "price": 100},
#     {"product": "Monitor", "price": 300},
#     {"product": "Chair", "price": 800},
#     {"product": "Desk", "price": 400}
# ]
# Пример вывода:
# ['Chair', 'Laptop']

orders = [
        {"product": "Laptop", "price": 1200},
        {"product": "Mouse", "price": 50},
        {"product": "Keyboard", "price": 100},
        {"product": "Monitor", "price": 300},
        {"product": "Chair", "price": 800},
        {"product": "Desk", "price": 400}
        ]

print("V1")
def filter_list(order : list[dict]):
    """
    Filters orders with price greater than 500,
    extracts product names, sorts them alphabetically,
    and returns the resulting list.

    Args:
        order (list[dict]): A list of orders with "product" and "price".
    Returns:
        list[str]: Sorted list of product names with price > 500.
    """
    filtered = [order["product"] for order in orders if order["price"] > 500]
    return sorted(filtered)
print(filter_list(orders))

print("V2 Lambda")
def filter_list2(order : list[dict]):
    """
    Filters orders with price greater than 500,
    extracts product names, sorts them alphabetically,
    and returns the resulting list.

    Args:
        order (list[dict]): A list of orders with "product" and "price".
    Returns:
        list[str]: Sorted list of product names with price > 500.
    """
    filter_list = map(lambda x: x["product"], filter(lambda x: x["price"] > 500, order))
    return sorted(filter_list)
print(filter_list2(orders))

# Задание 2
# Статистика продаж
# Дан список продаж в виде кортежей (товар, количество, цена).
# Напишите программу, которая:
#     Вычисляет общую выручку для каждого товара.
#     Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.
# Данные:
# sales = [
#     ("Laptop", 5, 1200),
#     ("Mouse", 50, 20),
#     ("Keyboard", 30, 50),
#     ("Monitor", 10, 300),
#     ("Chair", 20, 800)
# ]
# Пример вывода:
# {'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}

sales = [
        ("Laptop", 5, 1200),
        ("Mouse", 50, 20),
        ("Keyboard", 30, 50),
        ("Monitor", 10, 300),
        ("Chair", 20, 800)
        ]

def list_sales(sell : list[tuple]):
    """
    Calculates total revenue per product and returns
    a dictionary sorted by revenue in descending order.

    Args:
        sell (list[tuple]): (product, quantity, price)
    Returns:
        dict: {product: revenue} sorted by revenue (desc)
    """
    return dict(sorted(map(lambda x: (x[0], x[1] * x[2]), sell), key=lambda x: x[1], reverse=True))

print(list_sales(sales))