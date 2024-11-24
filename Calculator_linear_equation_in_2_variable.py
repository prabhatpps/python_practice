# Solve linear equation in 2 Variable


print("We are solving here linear equation in 2 variable")
print("Equation 1 is    n1 X + m1 Y = p1")
print("Equation 2 is    n2 X + m2 Y = p2")
n1 = float(input("n1 : "))
m1 = float(input("m1 : "))
p1 = float(input("p1 : "))
n2 = float(input("n2 : "))
m2 = float(input("m2 : "))
p2 = float(input("p2 : "))
value_of_x = (p1 * m2 - p2 * m1) / (n1 * m2 - m1 * n2)
value_of_y = (n1 * p2 - p1 * n2) / (n1 * m2 - m1 * n2)
print("Value of X = " + str(value_of_x))
print("Value of Y = " + str(value_of_y))
