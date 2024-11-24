L1 = [1, 2, (3, 4), 5, (6, 7), 8]
x = 0
for i in L1:
    if type(i) is tuple:
        x += 1
print(x)
