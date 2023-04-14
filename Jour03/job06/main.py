mot = "abcdefghijklmnopqrstuvwxyz" * 10
p = 1
i = 0

while i < len(mot):
    for j in range(p):
        if i>=len(mot):
            break
        print(mot[i], end=" ")
        i += 1
    print()
    p += 1