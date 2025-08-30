lst = [1, -2, 3, -4, 5]

for i in range(len(lst)):
    if lst[i] < 0:
        lst[i] = 0

print(lst)

