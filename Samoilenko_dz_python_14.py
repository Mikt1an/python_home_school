
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
new_strings = []
for string in strings:
    for numb in range(len(string)):
        if string[numb:].isdigit() and string[:numb].isalpha():
                new_strings.append(string)
print(new_strings)

numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
user_input = int(input("Enter a number to remove multiples of it: "))
remove_list = []
for number in numbers:
    if number%user_input == 0:
        remove_list.append(number)
for index in remove_list:
    numbers.remove(index)
print("list without multiples: ", numbers)

numbers = [5, 2, 3, 8, 4, 1, 2, 7]
print(numbers)
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
evens.sort(reverse=True)
result = []
i = 0
for n in numbers:
    if n % 2 != 0:
        result.append(n)
    else:
        result.append(evens[i])
        i += 1
print("list after sort:", result)
