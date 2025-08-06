def capl(s):
	word_list = s.split()
	capl_str = ""

	for i in range(0, len(word_list)):
		capl_str += (word_list[i][0].upper()+word_list[i][1::]+" ")

	return capl_str

a = input("Enter string : ")
print(capl(a))


