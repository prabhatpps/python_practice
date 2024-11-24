# print the number of letters of every word present in a input string


s = input("enter the string : ")
x = s.split(" ")
for i in x:
    print(i, '-', len(i), end="    ")
