import random
list1 = random.sample(range(100), random.randint(5, 20))
list2 = random.sample(range(100), random.randint(5, 20))


d = [i for i in list1 if i in list2]
d2 = [i for i in list1 if list1.count(i) == 1]

print d2