
text = "My number is 123-456-789"
print("line: ", text)

for num in text:
    if num.isdigit():
        text = text.replace(num, "*")
print(text)


text = "Programming in python"
print("line:", text)
text= text.lower()
checked = ""
for num in text:
    if num not in checked:
        count = text.count(num)
        if count > 1:
            print(f"Symbol '{num}' meet {count} times")
        checked += num


text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
text = text.split()
textnew = ""
for elem in text:
    if elem.isdigit():
        textnew += str(float(elem) * 10) + " "
        continue
    elif elem.find(".") != -1:
        spfloat = elem.split(".")
        if spfloat[0].isdigit() and spfloat[1].isdigit():
            textnew += str(float(spfloat[0] + "." + spfloat[1]) * 10) + " "
        else:
            textnew += elem + " "
    else:
        textnew += elem + " "
print(textnew)
