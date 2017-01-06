from time import time 

lookup = {}

# with prunning 
def stairs(n):
	if n in lookup:
		return lookup[n]
	if n < 0:
		return 0
	if n == 0:
		lookup[n] = 1
		return 1
	elif n > 0:
		next_depth_val = stairs(n-1) + stairs(n-2) + stairs(n-3)
		lookup[n] = next_depth_val
		return next_depth_val
		

# without prunning
def stairs_scrappy(n):
	if n < 0:
		return 0 
	if n == 0:
		return 1 
	return stairs_scrappy(n-1)+stairs_scrappy(n-2)+stairs_scrappy(n-3)



if __name__=="__main__":
	stamp = time()
	print stairs(100)
	print "with prunning took me", time() - stamp
	stamp = time()
	print stairs_scrappy(29)
	print "without prunning took me", time() - stamp

