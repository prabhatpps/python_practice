# Regular Expressions checking input reg. no., mobile no.,PAN no. is valid or not


import re

S1 = input("Reg.No.: ")
if re.search("^[0-9]{2}[a-zA-z]{3}[0-9]{4}$", S1):
    print("valid\n")
else:
    print("invalid\n")

S1 = input("mobile No.: ")
if re.search("^[1-9][0-9]{9}$", S1):
    print("valid")
else:
    print("invalid")

S1 = input("PAN No.: ")
if re.search("^[A-Z]{5}[0-9]{4}[A-Z]$", S1):
    print("valid")
else:
    print("invalid")
