# print the greatest number present in a list


L1 = [2, 8, 9, 3, 4]
x = 0
for i in L1:
    if x < i:
        x = i
print(x)
