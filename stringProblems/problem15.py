password = "Vellore@2025"

def strengthChecker(pwd):
	isLong = False
	hasLowercase = False
	hasUppercase = False
	hasDigit = False
	hasSpecial = False

	if len(pwd) >= 8:
		isLong = True

	if not pwd.isalnum():
		hasSpecial = True

	for i in pwd:
		if i.isupper():
			hasUppercase = True
		elif i.islower():
			hasLowercase = True
		elif i.isdigit():
			hasDigit = True

	return isLong and hasLowercase and hasUppercase and hasDigit and hasSpecial


print(strengthChecker(password))