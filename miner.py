from hashlib import sha256

def calc(num):
    return int(sha256(str(num)).hexdigest(), 16)


easy_difficulty = 13644220811252222222222222222222222222222222222222222222222222222222222222
current_difficulty = 1364422081125

for i in xrange(10000000):
    digest = calc(i)
    if digest <= easy_difficulty:
        print "Show us the money"
        break
    else:
        print i, digest
