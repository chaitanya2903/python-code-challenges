import random
from collections import Counter

def roll_dice(dice, trials = 100):
	count_dict = {}
	for roll in range(trials):
		x = sum([random.randint(1,sides) for sides in dice])
		if x in count_dict.keys():
			count_dict[x] += 1
		else:
			count_dict[x] = 1
	print(count_dict)
	print('Probability')
	for a in range(len(dice), sum(dice)+1):
		if a in count_dict.keys():
			print(a,count_dict[a]/trials)
		else:
			print(a,0)
roll_dice([6,6])