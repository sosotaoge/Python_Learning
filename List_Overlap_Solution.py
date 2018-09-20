# Regular problems


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

for x in a:
	if x in b:
		if x not in c: c.append(x)
print c



# Extra ones

import random
list1 = random.sample(range(100), random.randint(5, 20))
list2 = random.sample(range(100), random.randint(5, 20))
d = []

for y in list1:
	if y in list2:
		if y not in d: d.append(y)

print d
