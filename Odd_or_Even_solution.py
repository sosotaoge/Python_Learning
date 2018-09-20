# Regular problem

number = input("Please type in a number you want to check: ")
flag = number % 2
flag4 = number % 4


if flag == 0:
	print("this number is even")
else:
	print("this number is odd")




# Extras problem ------------- multiple of 4

flag_4 = number % 4
if flag4 == 0:
	print("this number is a multiple of 4")
else:
	print("this number is not a multiple of 4")


# num and check

num = input("Please enter a number as num: ")
check = input("Please enter a number as check: ")
num1 = str(num)
check1 = str(check)

if num % check == 0:
	print(num1 + " is evenly divided by " + check1)

else:
	print(num1 + " is not evenly divided by " + check1)