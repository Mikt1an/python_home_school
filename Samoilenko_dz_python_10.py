
cost = int(input("add price: "))
nom = [50, 10, 5, 2]
for nom in nom:
    coin = cost // nom
    cost -= nom * coin
    print(f"add coins {nom}: {coin}")


numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
print("list:", numbers)
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        continue
    else:
        numbers[i] = numbers[i] ** 2
print("Change list: ", numbers)
