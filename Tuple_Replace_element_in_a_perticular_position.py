T1 = (10, 20, 30, 40, 60, 50, 90, 100, 101)
T2 = ()
x = int(input("position : "))
for i in range(x - 1):
    T2 += (T1[i],)
y = input("tuple element : ")
T2 += (y,)
for i in range(x, len(T1)):
    T2 += (T1[i],)
print(T2)
