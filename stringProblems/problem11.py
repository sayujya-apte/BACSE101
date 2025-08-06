s = "aaabbcccc"

def compress(s):
	prev_char = s[0]
	prev_char_count = 0
	newstr = ""
	for i in range(0, len(s)):
		if s[i] != prev_char:
			newstr += prev_char+str(prev_char_count)
			prev_char = s[i]
			prev_char_count =1
		elif s[i] == prev_char:
			prev_char_count += 1

	newstr += prev_char+str(prev_char_count)

	return newstr

print(compress(s))
