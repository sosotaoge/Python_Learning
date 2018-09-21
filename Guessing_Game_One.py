from random import randint

Gnum = randint(1, 9)
num = input("Please guess a number in range [1, 9]: \n")
flag = 1

while True:
	if num < Gnum:
		print("Your guessing is too low!\n")
	elif num > Gnum:
		print("Your guessing is too high\n")
	elif num == Gnum:
		print("You got it! The number is " + str(Gnum) + '\n')
		break
	else:
		print("Your guessing number is invalid!\n")

	num = input("Please give another shot!")
	flag += 1

print("You have tried " + str(flag) + ' times to figure out the number!')