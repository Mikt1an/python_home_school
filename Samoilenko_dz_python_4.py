
value1 = int(input("Enter first value: "))
value2 = int(input("Enter second value: "))
print("and: ", bool(value1) and bool(value2))
print("or: ", bool(value1) or bool(value2))
print("not: ", not value1)
print("equal: ", value1 == value2)
print("not equal: ", value1 != value2)

light_input = input("Is the light on? (True/False): ")
window_input = input("Is the window open? (True/False): ")
print ("Is the light on? ", light_input == "True")
print ("Is the window open? ", window_input == "True")
print ("Are both conditions met? ", light_input == "True" and window_input == "True")
print ("Is at least one condition met? ", light_input != window_input)

tariff = 30
usemb = int(input("Please enter the used megabytes: "))
print("used megabytes: ", usemb)
print("tariff 500MB = ", tariff)
if usemb <= 500:
    print ("The used megabytes is less than 500 MB = 30 euro")
else:
    overtariff = (usemb - 500) * 0.2
    print ("The used megabytes is over than 500 MB = ", tariff + overtariff, "euro")



