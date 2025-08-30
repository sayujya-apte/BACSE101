lst = [[1,2], [3,4], [5]]
flat = []

for i in lst:
    for j in i:
        flat.append(j)

print(flat)
