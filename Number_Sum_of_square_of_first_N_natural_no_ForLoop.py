# sum of first n natural numbers using forloop


n = int(input("no. : "))
S = 0
for i in range(0, n + 1):
    S = S + (i * i)
print(S)
