# # sort the dictionary with respect to keys


D = {"a": 40, "c": 20, "d": 10, "b": 30}
key = list(D.keys())
key.sort()
X = {}
for i in key:
    X.update({i: D[i]})
print(X)
print(D.keys())