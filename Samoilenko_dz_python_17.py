
set1 = {1, 2, 3, 4}
set2 = {2, 3}

print("V1")
ress = True
for grade in set2:
    if grade not in set1:
        ress = False
        break
print("Sample output:", ress)

print("V2")
result = all(elem in set1 for elem in set2)
print("Sample output:", result)


set1 = {2, 3, 4, 5, 6}
set2 = {4, 5}
if set2.issubset(set1):
    print("subset: ", set2.issubset(set1))
    print("difference: ", set1.difference(set2))
elif set1.issubset(set2):
    print("subset: ", set1.issubset(set2))
    print("difference: ", set2.difference(set1))
