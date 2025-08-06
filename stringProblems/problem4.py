s = input("Enter a string : ")

newstr = ""

for i in s:
	if i.isalnum() or i == " ":
		newstr += i

print(newstr)
