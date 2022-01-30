import math

def is_prime(num):
	root = int(math.sqrt(num))
	if num == 0 or num == 1:
		return False
	for i in range (2, root):
		if num%i == 0:
			return False
	return True

num = int(raw_input("Enter the number you want factored: "))

factors = []

i = 2
while not is_prime(num):
	if is_prime(i):
		if num%i == 0:
			factors.append(i)
			num = num / i
	i += 1
factors.append(num)

print (factors)
