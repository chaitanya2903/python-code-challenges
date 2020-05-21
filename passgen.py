import json
from secrets import randbelow
def gen_password(num_words):
	file = open('passwords.txt','r')
	pass_str = file.read()
	pass_dict = json.loads(pass_str)
	password = list()
	for i in range(num_words):
		key = ''.join([str(randbelow(6)+1) for x in range(5)])
		password.append(pass_dict[key])
	print(' '.join(password))	 	



num_words = int(input("enter number of words: \n"))
gen_password(num_words)

