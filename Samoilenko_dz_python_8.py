
while True:
    selectinp = input("Entered symbol : ")
    if len(selectinp) != 1:
        continue
    print (f"Код Unicode: {ord(selectinp)}",
           f"ASCII symbol: {ord(selectinp) <= 127}",
           sep="\n")

text = input("Entered string: ")
indexfirst = int(input("Enter the starting index: "))
indexend = int(input("Enter the ending index: "))
sres = text[indexfirst:indexend]
if indexend > len(text):
    miss = indexend - len(text)
    sres += "_" * miss
print("Substring: ", sres)


text2 = input("Entered string: ")
textinp = input("Entered symbol: ")
i = 0
sres = 0
while i < len(text2):
    if text2[i] == textinp:
        sres += 1
    i += 1
print("Symbols meeting: ", sres)


text3 = input("Entered string: ")
x = text3[::-1]
i = 0
alltext = ""
while i < len(x):
    if x[i] not in "0123456789":
        alltext += x[i]
    i += 1
print(f"Result: {alltext}")
