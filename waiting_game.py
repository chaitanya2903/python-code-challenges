import time
import random
def game():
	target = random.randint(2,6)
	print("Your target time is" , str(target) , "seconds")
	input("Press enter to begin")
	start = time.perf_counter()
	input("Press enter again after " + str(target) + " seconds")
	elapsed = time.perf_counter() - start
	print("Elapsed time:" + str(elapsed))
	if elapsed == target:
		print("Perfect! Impeccable timing!")
	else:
		print("time difference:",str(elapsed - target))
while True:
	x = input("Press Y to play: ")
	if x == 'Y' or x == 'y':
		game()
	else:
		break