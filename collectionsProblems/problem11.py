lst = [1, 2, 3, 4]
perms = []

for i in range(len(lst)):
    rem = lst[i::]
    for j in rem:
        if lst[i] != j:
            perms.append((lst[i] ,j))

print(perms)
