ini = [1, 1]


def Fibonacci_generator(self = 'Please enter how many Fibonacci numbers you want to have: \n'):
	num = input(self)
	if num == 1: 
		return [1]
	elif num == 2:
		return [1, 1]
	elif num > 2:
		for x in xrange(2,num):
			ini.append(ini[x - 1] + ini[x - 2])
		return ini
	else:
		return 'You entered a invalid number!\n'

print Fibonacci_generator()