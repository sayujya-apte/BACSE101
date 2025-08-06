def checkPattern(s1, s2):
	chars = [c for c in s1]
	words = s2.split()
	mapping = {}

	status = True

	for i in range(0, len(chars)):
			if chars[i] not in list(mapping.keys()):
				mapping[chars[i]] = words[i]
			else:
				if mapping[chars[i]] != words[i]:
					status = False

	return status

print(checkPattern("abba", "dog cat cat dog"))
print(checkPattern("abba", "dog cat cat fish"))

