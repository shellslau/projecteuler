end = int(raw_input("enter the max number: "))
total = 0

for i in range (0, end):
	if (i%3 == 0):
		total += i
	elif (i%5 == 0):
		total += i

print total