from random import randint 
from sys import argv
import json 
import time 

RANDBOX = "randbox.json"


def create_box(exponent):
	randbox = [randint(0, 10**exponent) for x in range(10**exponent)]
	return randbox


def dumpbox(box, dump_filename):
	with open(dump_filename, "wb") as f:
		json.dump(box, f)


def readbox(dump_filename):
	with open(dump_filename, "rb") as f:
		return json.load(f)

box = readbox(RANDBOX)
print "done reading, array size: %s" % ("{:,}".format(len(box)))
stamp = time.time()
box.sort()
print "done sorting in %d seconds" % (time.time() - stamp)