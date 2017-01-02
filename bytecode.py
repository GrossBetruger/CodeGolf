

import dis 

def printxy():
	x = 'somestr'
	y = 'otherstr'
	return x + y

def x_range():
	gen = xrange(10)
	li = range(10)

print dis.dis(printxy)
# can't tell the difference because the dissambler doesn't know how range and xrange are implemented
print dis.dis(x_range)