words = ['apple', 'cat', 'bat', 'banana']

dic = {}

for i in words:
    if len(i) not in dic.keys():
        dic[len(i)] = [i]
    else:
        dic[len(i)].append(i)

print(dic)
