# take an input from user and say that is it a correct register No. or not


x = input("enter your Reg. No. : ")
reg_no = x.upper()
l = len(reg_no) == 9
x = reg_no[0:2].isdigit()
y = reg_no[2:5].isalpha()
z = reg_no[5:9].isdigit()
if l == True and x == True and y == True and z == True:
    print("Reg. No. is correct")
else:
    print("Reg. No. is Wrong")
