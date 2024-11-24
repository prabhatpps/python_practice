# Take two list as input 'Key and data' and make dictionary using corresponding index.


X = (input("Key : ")).split(",")
Y = (input("Data : ")).split(",")
set1 = {}
if len(X) == len(Y):
    c = 0
    while c < len(X):
        set1[X[c]] = Y[c]
        c = c + 1
print(set1)
for i in set1:
    print(i, set1[i])
