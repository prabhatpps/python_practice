# take two string as input and show that they are anagram or not, anagram => if two strings are made up of same letters
# and same no. of those letters then it is called anagram


st1 = input("1:")
st2 = input("2:")
stl1 = sorted(st1)
stl2 = sorted(st2)
if stl1 == stl2:
    print("yes")
else:
    print("no")
