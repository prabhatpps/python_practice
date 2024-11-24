# take a number by input and print the no. of digits in that number


n = int(input("no. : "))
count = 0
while n > 0:
    n = n // 10
    count = count + 1
print(count)
