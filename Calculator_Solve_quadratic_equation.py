# Solve the Quadratic Equation


print("We are here solving the Quadratic Equation : aX^2+bX+c")
a = float(input("value of a :"))
b = float(input("value of b :"))
c = float(input("value of c :"))
D = (b ** 2 - 4 * a * c) ** 0.5
x1 = (-b + D) / 2 * a
x2 = (-b - D) / 2 * a
print("X1 =" + str(x1) + " " + "X2 =" + str(x2))
