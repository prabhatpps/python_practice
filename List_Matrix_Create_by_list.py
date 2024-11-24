# Create a matrix by using input data.


rows = int(input("Enter the No. of rows : "))
columns = int(input("Enter the No. of columns : "))
L = []
for i in range(rows):
    L1 = []
    for j in range(columns):
        a = int(input("enter no. : "))
        L1.append(a)
    L.append(L1)
for k in L:
    for s in k:
        print(s, end=" ")
    print()
