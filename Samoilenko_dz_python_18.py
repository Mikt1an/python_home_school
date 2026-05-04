
numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
new_numbers = {numb for numb in numbers if numbers.count(numb) > 1}
print("Numbers that occur more than once: ", sorted(new_numbers, reverse=True))

dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}
print("The first dictionary is a subset of the second." if dict1.items() <= dict2.items() else "The first dictionary is not a subset of the second.")
print("The second dictionary is a subset of the first." if dict2.items() <= dict1.items() else "The second dictionary is not a subset of the first.")
