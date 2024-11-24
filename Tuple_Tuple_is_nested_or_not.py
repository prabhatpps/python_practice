x = (1, 2, 3, (1, 2, 4), 4, 5)
n = 0
for i in x:
    if type(i) is tuple:
        n = n + 1
if n > 0:
    print("nested")
if n == 0:
    print("not nested")
