# reverse the input string


a = input("input : ")
m = ""
for i in range(len(a) - 1, -1, -1):
    m = m + a[i]
print(m)
