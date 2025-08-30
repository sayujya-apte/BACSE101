lst = [1, 2, 3, 4, 5, 6]
dic = {"Even" : [], "Odd" : []}

for i in lst:
    if i&1 == 0:
        dic["Even"].append(i)
    else:
        dic["Odd"].append(i)

print(dic)
