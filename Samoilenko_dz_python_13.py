
numbers = (3, 7, 2, 8, 5, 10, 1)
print(numbers)
print(type(numbers))
newnumbers = []
maxnumb = numbers[0]
for numb in numbers:
    if numb >= maxnumb:
        newnumbers.append(numb)
        maxnumb = numb
my_tuple = tuple(newnumbers)
print(my_tuple)
print(type(my_tuple))


numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
print(numbers)
indexmax = {}
for index, number in enumerate(numbers):
    if number not in indexmax:
        indexmax[number] = []
    indexmax[number].append(index)
for index, value in indexmax.items():
    if len(value) > 1:
        print(f"Index {index}: ", *value)
