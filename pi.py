from math import sqrt
from operator import mul 

# Leibniz: 1 - 1/3 + 1/5 - 1/7 + 1/9 ... = pi/4

def calc_pi_leib(n):
	s = int()
	series = [1./x for x in range(1, n) if x % 2 == 1]
	for i in range(len(series)):
		if i % 2 == 0:
			s += series[i]
		else:
			s -= series[i]
	return 4 * s

print calc_pi_leib(int(1e7))

# Euler: 1/1 + 1/2 + 1/3 +1/4 ... = pi^2 / 6

def calc_pi_euler(n):
	return sqrt(6*(sum([(1./x)**2 for x in range(1, n)])))


print calc_pi_euler(int(1e6))

# From primes [without 2] (1 - 1/3) * (1 + 1/5) * (1- 1/7) * (1 - 1/11) * (1 + 1/13) = 2/pi
# the sign within the brackets - plus if the denominator holds (n*4 + 1) for a natural n
# else minus

def calc_pi_from_primes(n):
	primes = [x for x in range(3, n) if all([x % i != 0 for i in range(2, x)])]
	def is_multi4plus1(n):
		return (n-1) % 4 == 0
	series = [(1 + 1./x) if is_multi4plus1(x) else (1 - 1./x) for x in primes]
	return 2 / reduce(mul, series, 1) 


print calc_pi_from_primes(int(1e3))