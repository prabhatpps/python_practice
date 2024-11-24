# Regular Expressions Separate BEC students


import re

S = ["22BEC0072", "22BEC0074", "22BEC0083", "21BIT0086", "22BEC0698", "22BCS0056"]
k = []
for i in S:
    if re.search("^[0-9]{2}BEC[0-9]{4}$", i):
        k.append(i)
print(k)
