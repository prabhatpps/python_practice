# take 3 numbers as input from user and arrange in descending order


a = float(input("Enter the value of A = "))
b = float(input("Enter the value of B = "))
c = float(input("Enter the value of C = "))
if a > b and a > c:
    if b > c:
        print(str(a) + "," + str(b) + "," + str(c))
    else:
        print(str(a) + "," + str(c) + "," + str(b))
elif b > a and b > c:
    if a > c:
        print(str(b) + "," + str(a) + "," + str(c))
    else:
        print(str(b) + "," + str(c) + "," + str(a))
elif c > a and c > b:
    if a > b:
        print(str(c) + "," + str(a) + "," + str(b))
    else:
        print(str(c) + "," + str(b) + "," + str(a))
