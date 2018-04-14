from random import choice, randint
import operator as op


CHARACTERS = ["elf", "dork", "fork", "superwoman", "rick"]#, "42", "more", "that"]
THOUSAND_CHARACTERS = [str(x) for x in range(10**3)]


def grid(x, y):
    full_grid = []
    for i in xrange(x):
        for j in xrange(y):
            if i == j:
                continue
            full_grid.append((i, j))
    return full_grid


def full_random(characters):
    size = ncr(len(characters), 2)
    g = grid(len(characters), len(characters))
    print "combinatorial size is:", size
    while g:
        rand = randint(0, len(g)-1)
        i = g[rand]
        a, b = characters[i[0]], characters[i[1]]
        if a == b:
            continue
        a, b = list(sorted([a, b]))
        print a, b
        del g[rand]

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, xrange(n, n-r, -1), 1)
    denom = reduce(op.mul, xrange(1, r+1), 1)
    return numer//denom


if __name__ == "__main__":
    full_random(CHARACTERS)
    print
    print "number of characters:", len(CHARACTERS)
