keys = ['a', 'b', 'c']
values = [1, 2, 3]
dic = {}
if len(keys) == len(values):
    for i in range(len(keys)):
        dic[keys[i]] = values[i]**2

print(dic)
