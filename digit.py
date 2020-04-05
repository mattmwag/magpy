def sum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def has_2(l):
    return filter(lambda: 9 < n < 100, l)


def has_3(l):
    return filter(lambda n: 99 < n < 1000, l)


def first(n):
    return str(n)[0]


def second(n):
    return str(n)[1]


def third(n):
    return str(n)[2]
