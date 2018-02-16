from math import factorial as fac


def n_choose_k(n, k):
    return fac(n) \
           / (fac(k)*(fac(n - k)))


def birthday_probability(days, n):
    return 1 - ((fac(n) * n_choose_k(days, n)) \
           / float(days) ** n)


if __name__ == "__main__":
    print n_choose_k(255, 19)
    print birthday_probability(365, 5)
    print birthday_probability(365, 10)
    print birthday_probability(365, 20)
    print birthday_probability(365, 60)