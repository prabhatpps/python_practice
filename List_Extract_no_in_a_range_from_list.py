# Extract numbers from a list between the range that has given as input


L1 = [2, 4, 6, 8, 10]
L = []
lower_limit = 5
upper_limit = 10
for i in L1:
    if lower_limit < i <= upper_limit:
        L.append(i)
print(L)
