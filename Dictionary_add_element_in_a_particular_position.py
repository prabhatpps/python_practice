# add a dictionary element in a particular position as input


Dict_new = {"a": 10, "c": 3, "d": 4, "e": 6}
print(Dict_new)

# convert to list
alpha = []
for i in Dict_new:
    alpha.append([i, Dict_new[i]])

# taking inputs {key, value, position to place dictionary element at that position}
key_input = input("key: ")
value_input = input("value: ")
position = int(input("position: "))
final_dict = {}
n = 0
while n < position - 1:
    final_dict.update({alpha[n][0]: alpha[n][1]})
    n += 1
final_dict.update({key_input: value_input})
n = 0
while n < len(alpha):
    if n >= position - 1:
        final_dict.update({alpha[n][0]: alpha[n][1]})
    n += 1
print(final_dict)
