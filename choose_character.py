from random import choice
import operator as op


CHARACTERS = ["elf", "dork", "fork", "superwoman", "rick", "42", "more", "that"]
THOUSAND_CHARACTERS = [str(x) for x in range(10**3)]


def full_random(characters):
    matches = set()
    size = ncr(len(characters), 2)
    print "combinatorial size is:", size
    while size:
        a = choice(characters)
        b = choice(characters)
        if a == b:
            continue
        a, b = list(sorted([a, b]))
        if not ((a, b) in matches) and a != b:
            print a, b
            matches.update((a, b))
            size -= 1


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, xrange(n, n-r, -1), 1)
    denom = reduce(op.mul, xrange(1, r+1), 1)
    return numer//denom


if __name__ == "__main__":
    full_random(CHARACTERS)
    print
    print "number of characters:", len(CHARACTERS)
