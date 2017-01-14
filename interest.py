from itertools import combinations_with_replacement


def fall(n):
	return n * .9 


def rise(n):
	return n * 1.1


def dot(lst):
	val = 1 
	for i in lst:
		val *= i 
	return val


print rise(fall(100))
print fall(rise(100))


print 100 * .9 * 1.1
all_muls = list(combinations_with_replacement((0.9, 1.1), 10))
print all_muls
print len(all_muls)
for mul in all_muls:
	print 100 * dot(mul) 
print dot([.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9])

print list(combinations_with_replacement((1,2,3,4),2))