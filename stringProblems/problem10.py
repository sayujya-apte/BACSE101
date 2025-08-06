s = '''
	 Riviera is the flagship international sports and cultural festival of VIT Vellore, held annually in February. Spanning
	  four days, Riviera in 2025 featured over 45,000 students from 80 universities and colleges representing 26 countries 
	  in Asia, Europe and Africa. The festival features a vibrant mix of sports tournaments, cultural competitions, pro-shows, 
	  and social awareness events. The Riviera festival, has achieved both ISO certification and a Guinness World Record. 
	'''

char_freq = {}

for i in list(s):
	if i.isalnum():
		if i.lower() in list(char_freq.keys()):
			char_freq[i.lower()] += 1
		else:
			char_freq[i.lower()] = 1

print(char_freq)
