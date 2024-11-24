L1 = [(2, 3), (4, 5, 6), (7, 8), (9,)]
length_of_L1 = len(L1)
for i in range(length_of_L1):
    for j in range(len(L1[i])):
        L1.append(L1[i][j])
    L1[i] = "any random replace variable"
for k in range(length_of_L1):
    L1.remove("any random replace variable")
print(L1)
