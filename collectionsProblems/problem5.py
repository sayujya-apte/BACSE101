data = {'a' : 5, 'b' : 15, 'c' : 25}
filtered_data = {}

for i in data.keys():
    if data[i] > 10:
        filtered_data[i] = data[i]


print(filtered_data)

