# Solve Linear equation in 3 variable


print("We are solving here linear equation in 2 variable")
print("Equation 1 is    a1 X + b1 Y + c1 Z = d1")
print("Equation 2 is    a2 X + b2 Y + c2 Z = d2")
print("Equation 2 is    a3 X + b3 Y + c3 Z = d3")
a1 = float(input("a1 : "))
b1 = float(input("b1 : "))
c1 = float(input("c1 : "))
d1 = float(input("d1 : "))
a2 = float(input("a2 : "))
b2 = float(input("b2 : "))
c2 = float(input("c2 : "))
d2 = float(input("d2 : "))
a3 = float(input("a3 : "))
b3 = float(input("b3 : "))
c3 = float(input("c3 : "))
d3 = float(input("d3 : "))
value_of_x = (d1 * (b2 * c3 - c2 * b3) - b1 * (d2 * c3 - c2 * d3) + c1 * (d2 * b3 - b2 * d3)) / (
            a1 * (b2 * c3 - c2 * b3) - b1 * (a2 * c3 - c2 * a3) + c1 * (a2 * b3 - b2 * a3))
value_of_y = (a1 * (d2 * c3 - c2 * d3) - d1 * (a2 * c3 - c2 * a3) + c1 * (a2 * d3 - d2 * a3)) / (
            a1 * (b2 * c3 - c2 * b3) - b1 * (a2 * c3 - c2 * a3) + c1 * (a2 * b3 - b2 * a3))
value_of_z = (a1 * (b2 * d3 - d2 * b3) - b1 * (a2 * d3 - d2 * a3) + d1 * (a2 * b3 - b2 * a3)) / (
            a1 * (b2 * c3 - c2 * b3) - b1 * (a2 * c3 - c2 * a3) + c1 * (a2 * b3 - b2 * a3))
print("Value of X = " + str(value_of_x))
print("Value of Y = " + str(value_of_y))
print("Value of Z = " + str(value_of_z))
