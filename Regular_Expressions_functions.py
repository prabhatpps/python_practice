# Regular Expressions functions


import re

S1 = "Python is a programing language"
L1 = re.findall("on", S1)
L2 = re.findall("a", S1)
L3 = re.findall("Python", S1)
print(L1, "\n", L2, "\n", L3)
print(type(L1))

S1 = "Python is a programing language"
L1 = re.search("on", S1)
L2 = re.search("a", S1)
L3 = re.search("PYTHON", S1)
print(L1, "\n", L2, "\n", L3)
print(type(L1))

S1 = "Python is a programing language"
L1 = re.split(" ", S1)
L2 = re.split("a", S1)
L3 = re.split("PYTHON", S1)
print(L1, "\n", L2, "\n", L3)
print(type(L1))

S1 = "Python is a programing language"
L1 = re.sub("p", "P", S1)
L2 = re.sub("a", "A", S1)
L3 = re.sub("Python", "PYTHON", S1)
print(L1, "\n", L2, "\n", L3)
print(type(L1))
