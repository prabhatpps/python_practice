# Intersection of list as set


l1 = [1, 2, 5, 6, 8]
l2 = [1, 3, 5, 4, 7, 8]
l = l1 + l2
x = []
for i in l:
    if l.count(i) > 1:
        l.remove(i)
for i in l:
    if (i in l1) and (i in l2):
        x.append(i)
print(x)
