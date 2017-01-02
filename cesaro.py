from random import randint 
from math import sqrt


def gcd(a, b):
	if b == 0:
		return a 
	else:
		return gcd(b, a % b)


def get_rands(n):
	return randint(1, n), randint(1, n)


def cesaro():
	return gcd(*get_rands(60)) == 1


def monte_carlo(n_lst, experiment):
	return len(list(filter(lambda a : experiment(), n_lst)))/float(len(n_lst))


def estimate_pi(monte_carlo_prob):
	return sqrt(6/monte_carlo_prob)


print estimate_pi(monte_carlo(range(10**7), cesaro))
