
import math
number = float(input("Enter a number: "))
if number >= 0:
    result = math.floor(number + 0.5)
else:
    result = math.ceil(number- 0.5)
print("Rounded value:", result)

firstcatet = int(input("Enter first catet: "))
secondcatet = int(input("Enter second catet: "))
print ("Hypotenuse lenght: ", (firstcatet**2 + secondcatet**2) ** 0.5)
