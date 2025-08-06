s = "The year is 2025, and there are approximately 8.2 billion people on Earth. The temperature today is 25.5 degrees Celsius, and the time is 12:08."
int_list = []

for i in s:
	if i.isdigit():
		int_list.append(int(i))

print(int_list)
