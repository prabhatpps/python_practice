# Print parallelogram with number of *s taken as input


x = int(input("Enter number of rows : "))
t = input("Enter the symbol : ") + " "
n = 0
while n < x:
    print(" " * n + t * x)
    n = n + 1
