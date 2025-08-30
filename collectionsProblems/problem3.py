lst = ['apple', 'banana', 'apple', 'orange', 'banana']

freq = {}

for i in lst:
    if i not in freq.keys():
        freq[i] = 1
    else:
        freq[i] += 1

print(freq)
