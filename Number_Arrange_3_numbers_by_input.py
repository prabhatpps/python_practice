# take 3 numbers as input from user and then arrange it and print the combinations and the no. of combinations.


n1 = input("Enter the first number : ")
n2 = input("Enter the second number : ")
n3 = input("Enter the third number : ")
N1 = int(n1)
N2 = int(n2)
N3 = int(n3)
a = n1 + " " + n2 + " " + n3
b = n1 + " " + n3 + " " + n2
c = n2 + " " + n1 + " " + n3
d = n2 + " " + n3 + " " + n1
e = n3 + " " + n1 + " " + n2
f = n3 + " " + n2 + " " + n1
x = {a, b, c, d, e, f}
y = str(x)
m = (y.replace("{", ""))
n = (m.replace("}", ""))
k = (n.replace("'", ""))
if N1 == N2 != N3 or N2 == N3 != N1 or N3 == N1 != N2:
    print("No. of combinations are 3")
    print(k)
elif n1 == n2 == n3:
    print("No. of combinations are 1")
    print(k)
else:
    print("No. of combinations are 6")
    print(k)
