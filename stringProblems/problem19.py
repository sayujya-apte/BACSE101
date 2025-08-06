def longestSubstrWoRep(s):
	chars = []
	substr = ""
	unique_strs = []

	for i in s:
		if i not in chars:
			chars.append(i)
			substr += i
		else:
			unique_strs.append(substr)
			substr = i
			chars = [i]

	unique_strs.append(substr)

	max_len_substr = ""
	max_len = 0
	for j in unique_strs:
		if len(j) > max_len:
			max_len = len(j)
			max_len_substr = j

	print(unique_strs)
	return (max_len_substr)

print(longestSubstrWoRep("abcaderfgat"))



