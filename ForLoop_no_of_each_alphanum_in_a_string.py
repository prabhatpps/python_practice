# Print no. of each alphabet and numbers present in a string


s = "This is python2561"
s1 = ""
for i in s:
    if i.isalnum():
        if i not in s1:
            c = s.count(i)
            print(i, c)
            s1 = s1 + i
