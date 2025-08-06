s = '''
		VIT was established under Section 3 of the University Grants Commission Act, 1956, and was founded in 1984 
		by G. Viswanathan as a self-financing institution called the Vellore Engineering College. In 2001, It became 
		a deemed university.[9] In September 2006, it was renamed to VIT University. What truly sets VIT apart is 
		its student-centric approach. It was among the first in India to introduce the Fully Flexible Credit System (FFCS), 
		allowing students to choose their courses, faculty, and class schedules. This flexibility, combined with a strong 
		research ecosystem and global partnerships, has helped VIT consistently rank among the top private universities 
		in India and gain recognition in QS and Times Higher Education global rankings. 
	'''

word_count = {}

for i in s.split():
	if i in list(word_count.keys()):
		word_count[i] += 1
	else:
		word_count[i] = 1


print(word_count)