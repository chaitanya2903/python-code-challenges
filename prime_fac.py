def is_prime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	else:
		for i in range(2,n-1):
			if n%i == 0:
				return False
	return True
def get_prime_factors(n):
	li = list()
	for i in range(2,n+1):
		if is_prime(i) and n%i == 0:
			li.append(i)
	print(li)

x = int(input("Enter number: "))
get_prime_factors(x)