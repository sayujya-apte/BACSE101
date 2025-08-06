inp = ["act", "cat", "tac", "tap", "pat"] 

def findCharFreq(s):
	char_freq = {}

	for i in list(s):
		if i.isalnum():
			if i.lower() in list(char_freq.keys()):
				char_freq[i.lower()] += 1
			else:
				char_freq[i.lower()] = 1

	return char_freq
