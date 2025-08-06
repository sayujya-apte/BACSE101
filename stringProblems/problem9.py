s = '''
	The institution offers undergraduate and postgraduate, programmes. It has campuses in Vellore and Chennai and three
	sister universities as distinct state private universities in Amaravati, Bhopal, Bengaluru in India
	and an international campus in Mauritius.
	'''

max_lenth = 0
max_lenth_str = ""
for i in s.split():
	if len(i) > max_lenth:
		max_lenth = len(i)
		max_lenth_str = i

print(f"The longest word is {max_lenth_str} with a lenth of {max_lenth}")