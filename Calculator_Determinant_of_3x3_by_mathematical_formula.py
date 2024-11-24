# Solve 3X3 Determinant


print(
    "We are here solving the 3X3 determinant \n             d1  d2  d3\n             d4  d5  d6\n             d7  d8  "
    "d9")
d1 = float(input("Enter the value of d1 : "))
d2 = float(input("Enter the value of d2 : "))
d3 = float(input("Enter the value of d3 : "))
d4 = float(input("Enter the value of d4 : "))
d5 = float(input("Enter the value of d5 : "))
d6 = float(input("Enter the value of d6 : "))
d7 = float(input("Enter the value of d7 : "))
d8 = float(input("Enter the value of d8 : "))
d9 = float(input("Enter the value of d9 : "))
D = d1 * (d5 * d9 - d6 * d8) - d2 * (d4 * d9 - d6 * d7) + d3 * (d4 * d8 - d5 * d7)
print("The value of determinant is " + str(D))
