
firstnumber = int(input("Enter first number: "))
secondnumber = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
if firstnumber < secondnumber and firstnumber < number3:
    first = firstnumber
    if secondnumber < number3:
        second = secondnumber
        third = number3
    else:
        second = number3
        third = secondnumber
elif secondnumber < firstnumber and secondnumber < number3:
    first = secondnumber
    if firstnumber < number3:
        second = firstnumber
        third = number3
    else:
        second = number3
        third = firstnumber
else:
    first = number3
    if firstnumber < number3:
        second = firstnumber
        third = number3
    else:
        second = secondnumber
        third = number3
print ("Number 1: ", firstnumber)
print ("Numbers 2: ", secondnumber)
print ("Numbers 3: ", number3)
print ("Numbers in ascending order: ", first, second, third)

age = int(input("add age: "))
print ("This year is a leap year." if age % 4 == 0 and age % 100 != 0 or age % 400 == 0 else "The year is not a leap years.")
