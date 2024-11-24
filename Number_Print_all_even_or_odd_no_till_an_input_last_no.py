# take a number as input from user and print even or odd numbers till that number


n = int(input("last no. : "))
x = input("even or odd : ")
if x == "even":
    for i in range(2, n + 1, 2):
        print(i, end=" ")
elif x == "odd":
    for i in range(1, n + 1, 2):
        print(i, end=" ")
