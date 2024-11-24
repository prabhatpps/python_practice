# Addition of two matrix.


print("for matrix 1")
rows = int(input("Enter the No. of rows : "))
columns = int(input("Enter the No. of columns : "))
x = 0
y = 1
LA = []
for i in range(rows):
    L1 = []
    for j in range(columns):
        a = int(input("enter no. : "))
        L1.append(a)
    LA.append(L1)
print("for matrix 2")
rows = int(input("Enter the No. of rows : "))
columns = int(input("Enter the No. of columns : "))
x = 0
y = 1
LB = []
for k in range(rows):
    L2 = []
    for l in range(columns):
        a = int(input("enter no. : "))
        L2.append(a)
    LB.append(L2)
LK = []
for m in range(rows):
    L = []
    for n in range(columns):
        a = LA[m][n] + LB[m][n]
        L.append(a)
    LK.append(L)

print(LK)
