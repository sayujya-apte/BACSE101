def getCharFreq(a):
	char_count = []

	for i in list(s):
		if i != " ":
			if i in list(char_count.keys()):
				char_count[i] += 1
			else:
				char_count[i] = 1

	return char_count

s1 = input("Enter first string : ")
s2 = input("Enter second string : ")

if(getCharFreq(s1) == getCharFreq(s2)):
	print(f"\"{s1}\" and \"{s2}\" are anagrams")
else:
	print(f"\"{s1}\" and \"{s2}\" are not anagrams")