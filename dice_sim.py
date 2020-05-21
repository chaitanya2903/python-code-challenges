import random
from collections import Counter

def roll_dice(dice, trials = 10):
	count = Counter()
	for roll in range(trials):
		count[sum([random.randint(1,sides) for sides in dice])]  += 1
	print(count)
	print('Probability')
	for a in range(len(dice), sum(dice)+1):
		print(a,count[a]/trials)
roll_dice([6,6])