# Regular Expressions function elements


import re

S1 = "My name is Srinivas, none"
L1 = re.findall("Sr.", S1)
L2 = re.findall("Sr....", S1)
L3 = re.findall("n..e", S1)
print(L1, "\n", L2, "\n", L3,"\n")

S1 = "My name is srinivas"
S2 = "Python Programing"
L1 = re.findall("vas$", S1)
L2 = re.findall(".me$", S1)
L3 = re.findall("ing$", S2)
print(L1, "\n", L2, "\n", L3)
if re.search("srinivas$", S1):
    print("yes")
print("\n")

S1 = "ab a abc abbc abbbc abd abd"
S2 = "20BEC0934 20BEE0875 20BEI0567 20BCE0123"
L1 = re.findall("ab*", S1)
L2 = re.findall("ab*c", S1)
L3 = re.sub("ab*", "AB", S1)
print(L1, "\n", L2, "\n", L3,"\n")

S1 = "ab a abc abbc abbbc abd abd"
S2 = "20BEC0934 20BEE0875 20BEI0567 20BCE0123"
L1 = re.findall("ab+", S1)
L2 = re.findall("ab+c", S1)
L3 = re.sub("ab+", "AB", S1)
print(L1, "\n", L2, "\n", L3,"\n")

S1 = "ab a abc abbc abbbc abd abd"
S2 = "20BEC0934 20BEE0875 20BEI0567 20BCE0123"
L1 = re.findall("ab?", S1)
L2 = re.findall("ab?c", S1)
L3 = re.sub("ab?", "AB", S1)
print(L1, "\n", L2, "\n", L3,"\n")

S1 = "ab a abc abbc abbbc abd abd"
S2 = "20BEC0934 20BEE0875 20BEI0567 20BCE0123"
L1 = re.findall("ab{2}", S1)
L2 = re.findall("ab{3}c", S1)
L3 = re.sub("ab{1,4}", "AB", S1)
print(L1, "\n", L2, "\n", L3,"\n")

