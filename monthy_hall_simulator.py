from itertools import permutations
from random import choice, randint

CURTAINS = ["goat", "goat", "car"]
PERMS = list(set(list(permutations(CURTAINS))))
EXPERIMENT_SIZE = 100

def monthy_hall(switch_choice=False):
	game = choice(PERMS)
	player_choice = randint(0, 2)
	if not switch_choice:
		if game[player_choice] == "car":
			return True
		return False
	else:
		if game[player_choice] == "car":
			return False
		else:
			return True 

	

if __name__=="__main__":
	without_switching = [monthy_hall() for x in range(EXPERIMENT_SIZE)]
	with_switching = [monthy_hall(switch_choice=True) for x in range(EXPERIMENT_SIZE)]
	print without_switching
	print with_switching
	total = float(EXPERIMENT_SIZE)
	print "no switch", len([x for x in without_switching if x])/total
	print "with switch", len([x for x in with_switching if x])/total