

prefix = ""

for i in range(len(strs[0])):
    ch = strs[0][i]
    found = True

    for j in range(1, len(strs)):
        if i >= len(strs[j]) or strs[j][i] != ch:
            found = False
            break

    if found:
        prefix += ch
    else:
        break

print(prefix)
