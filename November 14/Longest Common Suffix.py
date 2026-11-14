

suffix = ""

for i in range(1, len(strs[0]) + 1):
    ch = strs[0][-i]
    found = True

    for j in range(1, len(strs)):
        if i > len(strs[j]) or strs[j][-i] != ch:
            found = False
            break

    if found:
        suffix += ch
    else:
        break

print(suffix[::-1])
