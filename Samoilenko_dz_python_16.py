
print("V1")
grades = [5, 3, 4, 2, 1, 5, 3]
ress = []
for grade in grades:
    match grade:
        case 5:
            ress.append([grade, "Excellent"])
        case 3 | 4:
            ress.append([grade, "Good"])
        case _:
            ress.append([grade, "Unsatisfactory"])
print(ress)

print("V2")
ress = [[grade, "Excellent" if grade == 5 else "Good" if grade in (3, 4) else "Unsatisfactory"] for grade in grades]
print(ress)

# string = "({[}])"
# string = ""
# string = " "
# string = "123"
string = "([({}()){}])"
print("hooks", string)
if not string:
    result = False
else:
    while True:
        new_strings = string.replace("()","").replace("[]","").replace("{}","")
        if new_strings == string:
            break
        string = new_strings
    result = (string == "")
print("valid: ", result)
