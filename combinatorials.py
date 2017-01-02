from itertools import combinations 


words = ["here", "is", "for", "the", "crazy", "ones"]


def n_choose_k(n_collection, k):
	return list(combinations(n_collection, k))


def n_choose_k_gen(n_collection, k):
	raw_comb = combinations(n_collection, k)
	try:
    		while True:
		    	item = next(raw_comb)
		    	yield item
	except StopIteration:
	    pass


def powerset(_set, non_empty=True):
	power_set = [list(combinations(_set, n)) for n in range(len(_set)+1)]
	if non_empty:
		return power_set[1:]
	return power_set


if __name__=="__main__":
	combos = n_choose_k(words, 2)
	print combos
	raw_comb = combinations(words, 3)
	combos_gen = n_choose_k_gen(words, 2)
	for comb in combos_gen:
		print comb

	print "\n"
	for s in powerset(words, non_empty=False):
		print s