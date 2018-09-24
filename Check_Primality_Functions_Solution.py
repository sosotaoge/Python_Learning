def prime_check(help_text = "Enter a number to check whether it is a prime number: \n"):
	num_check = input(help_text)
	divisor = []
	for x in xrange(2, (num_check / 2) + 1):
		if num_check % x == 0:
			divisor.append(x)
	if not divisor:
		print('the number you enter is a prime number')
	else:
		print('the number you enter is a prime number, and its divisor is: ' + str(divisor))

prime_check()