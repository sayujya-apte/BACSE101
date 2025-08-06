inp = input("Enter any string : ")
vowels = "aeiou"
char_counts = {"V" : 0, "C" : 0}

for i in inp:
	if i.isalpha():
		if i.lower() in vowels:
			char_counts["V"] += 1
		else:
			char_counts["C"] += 1

print(char_counts) 