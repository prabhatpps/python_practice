L = [(), (1, 2), (), (3, 4), (5, 6), (), (7, 8)]
L2 = []
for i in L:
    if len(i) != 0:
        L2.append(i)
print(L2)
