# Swap keys and values in a dictionary


D = {"a": 10, "b": 20, "c": 30}
x = {}
for i in D:
    x.update({D[i]: i})
print(x)
