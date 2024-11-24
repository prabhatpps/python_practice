# Print L2 from L1 as list L2 contains lists of same index elements
# Ex,L1 = [["Harish", "22BEC0950", "8.5"], ["Animesh", "22BEC0950", "8.3"]]
# => L2 = [["Harish", "Animesh"], ["22BEC0950", "22BEC0950"], ["8.5", "8.3"]]


L = [["Harish", "22BEC0950", "8.5"], ["Animesh", "22BEC0951", "8.3"]]
rows = len(L)
columns = len(L[0])
L2 = []
for i in range(columns):
    L3 = []
    for j in range(rows):
        n = L[j][i]
        L3.append(n)
    L2.append(L3)
print(L2)
