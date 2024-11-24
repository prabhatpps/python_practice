# take a number as input from user and say that if it is prime or not


print("Find given No. is Prime or None-Prime")
n = int(input("Enter your No. : "))
a = 1
c = 0
while a <= n:
    if n % a == 0:
        c = c + 1
    a = a + 1
if c == 2:
    print("prime")
else:
    print("non prime")
