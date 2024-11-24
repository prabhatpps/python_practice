# print how many alpha bets and numbers are there in a string


s = input("Enter the String : ")
d = 0
a = 0
for i in s:
    if i.isalpha():
        a = a + 1
    if i.isnumeric():
        d = d + 1
print("No. of alphabets = ", a, "and", "No. of numbers = ", d)
