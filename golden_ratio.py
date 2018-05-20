def golden(x, n):
    for _ in range(n):
        x = 1 + (1. / x)
    return x


if __name__ == "__main__":
    print golden(234.3, 100)
    print golden(-13, 100)
