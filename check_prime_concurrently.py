from math import sqrt, ceil 
from multiprocessing import Pool


def is_prime(n):
	if n == 2:
		return True
	elif n in set([0,1,4]):
		return False
	return all([n % x != 0 for x in range(2, int(ceil(sqrt(n)))+1)])


for i in range(20):
	print i, is_prime(i)

if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, [1, 2, 3]))