

found = True

if len(prefix) > len(s):
    found = False
else:
    for i in range(len(prefix)):
        if prefix[i] != s[i]:
            found = False
            break

if found:
    print("True")
else:
    print("False")
