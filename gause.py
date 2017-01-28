from random import choice
import numpy as np
import scipy.stats as stats
import pylab as pl

left, right = -1, 1


def trickle_down(balls, depth):
	assert(depth % 2 == 1)
	buttom = [0]*depth*2
	for i in range(balls):
		place = depth-1 
		for i in range(depth-1):
			place += choice([left, right])
		buttom[place] += 1
	return [buttom[x] for x in range(len(buttom)) if x % 2 != 1]


def flatten(l):
	def flat(l):
		for i in l:
			for j in i:
				yield j
	return list(flat(l))


if __name__=="__main__":
	trickled_balls = trickle_down(1000, 11)
	dist = flatten([[i]*x for i, x in enumerate(trickled_balls)])
	print trickled_balls
	print dist
	fit = stats.norm.pdf(dist, np.mean(dist), np.std(dist)) 

	pl.plot(dist, fit, '-o')

	pl.hist(dist, normed=True) 

	pl.show() 
