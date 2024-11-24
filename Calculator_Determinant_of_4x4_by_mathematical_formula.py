# Solve 4X4 Determinant


print("We are here solving the 4x4 determinant \n          d1   d2   d3   d4\n          d5   d6   d7   d8\n          "
      "d9   d10  d11  d12\n          d13  d14  d15  d16")
d41 = float(input("Enter the value of d1 : "))
d42 = float(input("Enter the value of d2 : "))
d43 = float(input("Enter the value of d3 : "))
d44 = float(input("Enter the value of d4 : "))
d45 = float(input("Enter the value of d5 : "))
d46 = float(input("Enter the value of d6 : "))
d47 = float(input("Enter the value of d7 : "))
d48 = float(input("Enter the value of d8 : "))
d49 = float(input("Enter the value of d9 : "))
d410 = float(input("Enter the value of d10 : "))
d411 = float(input("Enter the value of d11 : "))
d412 = float(input("Enter the value of d12 : "))
d413 = float(input("Enter the value of d13 : "))
d414 = float(input("Enter the value of d14 : "))
d415 = float(input("Enter the value of d15 : "))
d416 = float(input("Enter the value of d16 : "))

d1 = d46
d2 = d47
d3 = d48
d4 = d410
d5 = d411
d6 = d412
d7 = d414
d8 = d415
d9 = d416
Da = d1 * (d5 * d9 - d6 * d8) - d2 * (d4 * d9 - d6 * d7) + d3 * (d4 * d8 - d5 * d7)
aa = Da

d1 = d45
d2 = d47
d3 = d48
d4 = d49
d5 = d411
d6 = d412
d7 = d413
d8 = d415
d9 = d416
Db = d1 * (d5 * d9 - d6 * d8) - d2 * (d4 * d9 - d6 * d7) + d3 * (d4 * d8 - d5 * d7)
bb = Db

d1 = d45
d2 = d46
d3 = d48
d4 = d49
d5 = d410
d6 = d412
d7 = d413
d8 = d414
d9 = d416
Dc = d1 * (d5 * d9 - d6 * d8) - d2 * (d4 * d9 - d6 * d7) + d3 * (d4 * d8 - d5 * d7)
cc = Dc

d1 = d45
d2 = d46
d3 = d47
d4 = d49
d5 = d410
d6 = d411
d7 = d413
d8 = d414
d9 = d415
Dd = d1 * (d5 * d9 - d6 * d8) - d2 * (d4 * d9 - d6 * d7) + d3 * (d4 * d8 - d5 * d7)
dd = Dd

D4 = d41 * aa - d42 * bb + d43 * cc - d44 * dd
print("The value of determinant is " + str(D4))
