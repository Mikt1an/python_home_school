
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
