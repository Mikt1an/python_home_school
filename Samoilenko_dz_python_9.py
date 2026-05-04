
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i*j:2}", end=" ")
    print()

num = int(input("Enter a number: "))
n = ""
for i in range(1, num + 1):
    n += str(i) + " "
    print(n, end="\n")

text = input("Enter a string: ")
result = ""
for t in text:
    if t not in result:
        result += t
print("Result: ", result)
