emp = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9]



#Loop solutions:

def loop1(n):
	n1 = []
	for x in emp:
		if x not in n1:
			n1.append(x)
	return n1

#Set solutions:

def set1(n):
	return list(set(n))


print str(loop1(emp)) + '\n'
print set1(emp)