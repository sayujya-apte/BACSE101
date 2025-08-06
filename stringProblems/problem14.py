def is_substr(string, substr):
	for i in range(0, len(string) - len(substr) + 1):
		if string[i:i+len(substr)] == substr:
			return True

	return False


str1 = input("Enter string : ")
str2 = input("Enter substring : ")
print(is_substr(str1, str2))