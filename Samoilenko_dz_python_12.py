
numbers = [1245.4435, -302.1403, 87459.99, -520.8265, 1450.001]
print(numbers)
summa = 0
for num in numbers:
    if num > 0:
        summa += num
print("${:,.2f}".format(summa))

data_list = [
    "John 23 12345.678",
    "Alice 30 200.50",
    "Bob 35 15000.3",
    "Charlie 40 500.75"
    ]
for data in data_list:
    name, age, balance = data.split()
    print(f"Name: {name:<10} | age:{age:>3} | balance:{float(balance):>10.2f}")
