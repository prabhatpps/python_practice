# Create transpose of a matrix by using input data.


rows = int(input("Enter the No. of rows : "))
columns = int(input("Enter the No. of columns : "))
x = 0
y = 1
L = []
for i in range(rows):
    L1 = []
    for j in range(columns):
        a = int(input("enter no. : "))
        L1.append(a)
    L.append(L1)
print(L)
X = []
for k in range(columns):
    X2 = []
    for l in range(rows):
        n = L[l][k]
        X2.append(n)
    X.append(X2)
print(X)
