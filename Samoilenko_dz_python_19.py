
data = {"a": 1, "b": 2, "c": 1, "d": 3}
revers_data = {}
for key, item in data.items():
    if item not in revers_data:
        revers_data[item] = [key]
    else:
        revers_data[item].append(key)
print("Reversed dictionary:", revers_data)

words = ["anna", "bennet", "john"]
result =  {}
for word in words:
    let = {}
    for letter in set(word):
        let[letter] = word.count(letter)
    result[word] = let
print(result)

print("V1")
students = {"Anna": 92, "Borya": 76, "Vanya": 65, "Galya": 48, "Dima": 88, "Eva": 54}
groups = ["Excellent students", "Good students", "C students", "Failed"]
gro = {}
for group in groups:
    sum_group = {}
    for student in students.keys():
        if students[student] >= 85 and group == "Excellent students":
            sum_group[student] = students[student]
        elif 84 >= students[student] >= 70 and group == "Good students":
            sum_group[student] = students[student]
        elif 69 >= students[student] >= 50 and group == "C students":
            sum_group[student] = students[student]
        elif students[student] < 50 and group == "Failed":
            sum_group[student] = students[student]
    gro[group] = sum_group
print(gro)

print("V2")
gro = {group: {} for group in groups}
for student in students:
    score = students[student]
    if score >= 85:
        gro["Excellent students"][student] = score
    elif score >= 70:
        gro["Good students"][student] = score
    elif score >= 50:
        gro["C students"][student] = score
    else:
        gro["Failed"][student] = score
print(gro)
