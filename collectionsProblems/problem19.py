students = [{'name' : 'A', 'grade' : 'X'}, {'name' : 'B', 'grade' : 'Y'}, {'name' : 'C', 'grade' : 'X'}]

grp = {}

for i in students:
    if i['grade'] not in grp.keys():
        grp[i['grade']] = [i['name']]
    else:
        grp[i['grade']].append(i['name'])

print(grp)
