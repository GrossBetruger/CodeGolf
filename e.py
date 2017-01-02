
E = 2.7182818284590452353602874713527




def get_first_mismatch_index(num, expected_num):
	num = str(num)
	expected_num = str(expected_num)
	assert len(expected_num) >= len(num)
	for i, d in enumerate(num):
		if num[i] != expected_num[i]:
			return i
	return len(num)

# paint accurate digits green and the rest red (in terminal)
def paint_accuracy(num, constant):
	class bcolors:
	    HEADER = '\033[95m'
	    OKBLUE = '\033[94m'
	    OKGREEN = '\033[92m'
	    WARNING = '\033[93m'
	    FAIL = '\033[91m'
	    ENDC = '\033[0m'
	    BOLD = '\033[1m'
	    UNDERLINE = '\033[4m'
	num_str = str(num)
	break_index = get_first_mismatch_index(num, constant)
	return bcolors.OKGREEN + num_str[0:break_index] + bcolors.ENDC \
		   + bcolors.FAIL + num_str[break_index:] + bcolors.ENDC


# Euler: e = 1 + 1/1! + 1/2! + 1/3! ... 

def calc_euler_e(n):
	def fac(a):
		if a == 1:
			return a
		return a * fac(a-1)
	return 1 + sum([1./fac(x) for x in range(1, n)])

e = calc_euler_e(int(1e1))
print paint_accuracy(e, E)


# Euler: e = 2 + 1/(1 + 1/(2 + 1/(1 + 1/(1 + 1/(4 + 1/(...))))))

def recur_frac(n):
	inflate_string = "2 + 1./(1 + $)"
	numbers = [2*(x/3) if x % 3 == 0 else 1 for x in range(2, n)]
	for i in numbers[1:]:
		inflate_string = inflate_string.replace("$", "1./(# + $)").replace("#", str(i))
	return eval(inflate_string.replace("$", "0"))

e = recur_frac(13)
print paint_accuracy(e, E)

