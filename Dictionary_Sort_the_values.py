# sort the dictionary with respect to values


# swap keys and values
D = {"a": 10, "c": 3, "d": 4, "e": 6}
x = {}
for i in D:
    x.update({D[i]: i})

# sort the keys which is previously values
key = list(x.keys())
key.sort()
X = {}
for i in key:
    X.update({i: x[i]})

# swap keys and values
t = {}
for i in X:
    t.update({X[i]: i})
print(t)
