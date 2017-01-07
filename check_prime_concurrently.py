from math import sqrt, ceil 
from multiprocessing.dummy import Pool
from multiprocessing import cpu_count
from time import time, sleep


def is_prime(n, thread_count):
	if n in set([2, 3]):
		return True
	elif n in set([0,1,4]):
		return False

	check_range = range(2, int(ceil(sqrt(n)))+1)
	chunk_size = len(check_range)/thread_count
	chunked_jobs = list(chunker(check_range, chunk_size))

	chunked_jobs_args = [(n, x) for x in chunked_jobs]
	p = Pool(thread_count)
	results = p.map(is_prime_range, chunked_jobs_args)
	return all(results)
  

def is_prime_range(job):
	n = job[0]
	start = job[1][0]
	end = job[1][-1] + 1
	return all([n % x != 0 for x in range(start, end)])


def is_prime_one_threaded(n):
	if n in set([2, 3]):
		return True
	elif n in set([0,1,4]):
		return False

	check_range = range(2, int(ceil(sqrt(n)))+1)
	return all([n % x != 0 for x in check_range])


def chunker(lst, size):
	while lst:
		yield lst[:size]
		lst = lst[size:]


def take_time(func, args):
	stamp = time()
	print func(*args)
	print "took", time() - stamp


if __name__ == '__main__':
	BIGNUM = 218714987212989
	HUGE_PRIME = 1530692068127007263
	cores = cpu_count()
	take_time(is_prime, (BIGNUM, cores))
	# quit()
	take_time(is_prime_one_threaded, (BIGNUM,))