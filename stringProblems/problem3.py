s = input("Enter string : ")

def rev_str(a):	
	rev = ""
	for i in range(len(a)-1, -1, -1):
		rev += a[i]
	return rev

if s == rev_str(s):
	print(f"{s} is a palindrome")
else:
	print(f"{s} is not a palindrome")