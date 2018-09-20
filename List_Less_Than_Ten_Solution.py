a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Regular problems
for x in a:
	if x < 5:
		print x


# Extra ones
b = []
for y in a:
	if y < 5:
		b.append(y)
print b


c = []
num = input("Please enter a num: ")

for z in a:
	if z < num:
		c.append(z)
print c