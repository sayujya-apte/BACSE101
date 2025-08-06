roman = {
	"I" : 1,
	"V" : 5,
	"X" : 10,
	"L" : 50,
	"C" : 100,
	"D" : 500,
	"M" : 1000
}

def romanToInt(s):
	s = list(s)
	value = 0
	i = 0

	while(i < len(s)):
		a = roman[s[i]]
		
		if(i+1 < len(s)):
			b = roman[s[i+1]]

			if a >= b:
				value += a
				i += 1

			else:
				value = value + b - a
				i += 2
		else:
			value += a
			i += 1

	return value
	
# PENDING : CHECKING VALIDITY OF ROMAN NUMERAL
print(romanToInt("VIII")) 