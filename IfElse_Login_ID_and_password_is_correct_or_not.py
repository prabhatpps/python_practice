# your Login ID is student and Password is ece. take Login ID as input form user if it is correct then ask for
# Password, if both Login ID and Password are correct then print welcome and print your password is expired and
# take new Password is input and them print both Login ID and new Password


x = "student"
y = "ece"
login = input("Login ID : ")
if login == x:
    password = input("Password : ")
    if password == y:
        print("welcome")
        print("you password is expired. change your password")
        new_password = input("Enter your new password : ")
        print("Login ID : " + str(login))
        print("Password : " + str(new_password))
    else:
        print("Wrong Password")
else:
    print("Wrong Login ID")
