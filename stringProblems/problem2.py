s = input("Enter any string : ")

full_rev = ""

for i in range(len(s)-1, -1, -1):
	full_rev += s[i]

print(f"Full Reverse : {full_rev}")

inp_rev = ""
words = s.split()

for word in words:
	words_rev = ""
	for i in range(len(word)-1, -1, -1):
		words_rev += word[i]
	inp_rev += words_rev
	inp_rev += " "

print(f"In-place Reverse : {inp_rev}")