# Create dictionary by taking input data and convert the elements to list.


X = "yes"
set1 = {}
if X == "yes":
    while X == "yes":
        Key = (input("Key : "))
        Data = (input("Data : "))
        set1[Key] = Data
        X = input("Want to add data : ")
print(set1)
for i in set1:
    y = [i, set1[i]]
    print(y, end=" ")
