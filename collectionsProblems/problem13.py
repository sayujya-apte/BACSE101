dic = {'a' : 1, 'b': 2, 'c' : 2, 'd' : 3}
dic_unq = {}

for i in dic.keys():
    if dic[i] not in dic_unq.values():
        dic_unq[i] = dic[i]
    else:
        k = ''
        for key, value in dic_unq.items():
            if value == dic[i]:
                k = key
        dic_unq.pop(k)

print(dic_unq)
