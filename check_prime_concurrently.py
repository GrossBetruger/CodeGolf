from math import sqrt, ceil 
from multiprocessing.pool import Pool
from multiprocessing import cpu_count
from time import time, sleep


def is_prime(n, thread_count, chunked_jobs):
	if n in set([2, 3]):
		return True
	elif n in set([0,1,4]):
		return False

	p = Pool(thread_count)
	results = p.map(is_prime_range, chunked_jobs)
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


def take_time(func, args, print_res=True):
	stamp = time()
	print func(*args)
	print func.__name__ + " took", time() - stamp



def job_creator(n):
	check_range = range(2, int(ceil(sqrt(n)))+1)
	chunk_size = len(check_range)/500
	chunked_jobs = list(chunker(check_range, chunk_size))
	return [(n, x) for x in chunked_jobs]


if __name__ == '__main__':
	BIGNUM = 218714987212989
	BIG_PRIME = 727777887889889
	HUGE_PRIME = 1530692068127007263
	print "preparing data... it will take a while"
	stamp = time()
	cores = cpu_count()
	chunked_jobs = job_creator(BIGNUM)
	print "preparing data took",  time() - stamp
	take_time(is_prime, (BIGNUM, cores, chunked_jobs))
	take_time(is_prime_one_threaded, (BIGNUM,))