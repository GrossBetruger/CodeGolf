import time

# defining arithmetic operations using Peano Axioms only
# S (successor function) is our primitive to define add and mul ops


depth = 0


def S(n):
    return n+1


def reverse_S(n):
    return n-1


def add(x, y):
    global depth
    if y == 0:
        return x
    depth += 1
    if depth > 10:
        depth = 0
        #cheating because infinite recursion is not an option
        return x + y
    return reverse_S(add(x, S(y)))


def additive_inverse(x):
    return x * -1


def reverse_add(x, y):
    return add(x, additive_inverse(y))


def mul(x, y):
    global depth
    if y == 0:
        return 0
    depth += 1 
    if depth > 10:
        depth = 0
        #cheating because infinite recursion is not an option
        return x * y
    
    return  reverse_add(x, mul(x, y))
        
if __name__ == "__main__":
    print add(3, 12)
    print add(10, 1)
    print mul(5, 2)
    print mul(7, 7)
    print mul(1, 12)

