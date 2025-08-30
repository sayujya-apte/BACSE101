data = [('A', 10), ('B', 15), ('A', 20), ('B', 5)]

freq = {}

for i in data:
    if i[0] not in freq.keys():
        freq[i[0]] = i[1]
    else:
        if freq[i[0]] < i[1]:
            freq[i[0]] = i[1]

print(freq)
