
numbers = input("Please enter a four-digit number: ")
sumnumbers = int(numbers[0]) + int(numbers[1]) + int(numbers[2]) + int(numbers[3])
print(f"Sum of the digits of the number: {sumnumbers}")

firstnumber = int(input("Please enter the first number: "))
secondnumber = int(input("Please enter the second number: "))
print ("Result", end=': ')
print (firstnumber * secondnumber, firstnumber, secondnumber, sep='-')

firstnumber2 = int(input("Please enter the first number: "))
secondnumber2 = int(input("Please enter the second number: "))
integerdiv = int(firstnumber2 / secondnumber2)
remainderdiv = firstnumber2 - (secondnumber2 * integerdiv)
print (f"Remainder of the division: {remainderdiv}\nInteger division result: {integerdiv}")
