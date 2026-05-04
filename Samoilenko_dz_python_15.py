
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
for symbol in text_list[:]:
    if symbol.find(" ") != -1:
        text_list.remove(symbol)
    else:
        index = text_list.index(symbol)
        text_list[index] = symbol.lower()
print(text_list)

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
rabat = int(input("Enter discount (in procent): ")) / 100
print(f"{"Name":<10}", f"{"Old Price":>11}", f"{"New Price":>15}")
for product in products:
    new_price = product[1] - (product[1] * rabat)
    index = products.index(product)
    products[index] = [product[0], product[1], new_price]
for name, old_price, new_price in products:
    print(f'{name:<10}{old_price:>11.2f}${new_price:>15.2f}$')
