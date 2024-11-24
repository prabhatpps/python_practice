# Print hexagon with number of *s taken as input


x = int(input("Enter number of rows : "))
t = input("Enter the symbol : ") + " "

k = 0
while k < x:
    print(" " * (x - k) + t * k)
    k = k + 1

m = 0
while m < (x - 1):
    print(t * x)
    m = m + 1

n = 0
while n < x:
    print(" " * n + t * (x - n))
    n = n + 1
