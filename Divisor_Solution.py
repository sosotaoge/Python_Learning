num = input("Please enter a number you like: ")
a = xrange(1, num+1)
divisor = []


for x in a:
	if num % x == 0:
		divisor.append(x)
print divisor