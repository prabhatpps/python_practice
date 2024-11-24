D = {"22BEC0083": "Prabhat Pandey", "22BEC0072": ["Pranjal", "sahil"]}
print("old = ", D)
D["22BEC0074"] = "Parth"
print("new = ", D)
print(type(D))

for i in D:
    print(i, " : ", D[i])
for j in D["22BEC0072"]:
    print(j)
print(D["22BEC0072"][1], D["22BEC0072"][0])
del D['22BEC0083']
print(D)
X = D.copy()
del X['22BEC0074']
print(X)
print(D)
