# print all th prime no. between a range that was in input


lower = int(input("lower limit : "))
upper = int(input("upper limit : "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            # divisor never be 1 or itself so if any divisor be there then it will be non-prime
            if (num % i) == 0:
                break
        else:
            print(num, end=", ")
