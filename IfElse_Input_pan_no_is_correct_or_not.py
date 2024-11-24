# Take an input from user and say that is it a correct PAN card No. or not


x = input("enter your PAN No. : ")
panno = x.upper()
l = len(panno) == 10
x = panno[0:5].isalpha()
y = panno[5:9].isdigit()
z = panno[9:10].isalpha()
if (l == True) and (x == True) and (y == True) and (z == True):
    print("PAN No. is correct")
else:
    print("PAN No. is Wrong")
