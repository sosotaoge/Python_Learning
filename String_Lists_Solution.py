string = input("Please enter a string: ")

reverse = string[: : -1]

if string == reverse:
	print 'This string is a palindrome'
else:
	print 'This string is not a palindrome'