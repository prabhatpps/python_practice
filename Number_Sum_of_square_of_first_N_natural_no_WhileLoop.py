# sum of first n natural numbers using whileloop


n = int(input("no. : "))
sum1 = 0
i = 0
while i <= n:
    sum1 = sum1 + (i * i)
    i = i + 1
print(sum1)
