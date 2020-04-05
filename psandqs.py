from primes import primes
from candidates import candidates


def smallest_prime_nonfactor(n):
    ps = primes(1000)
    for p in ps:
        if n % p > 0:
            return p
    return "Not found"


def smallest_prime_nonfactor_(ns):
    ps = primes(1000)
    for p in ps:
        factor = False
        for n in ns:
            if n % p == 0:
                factor = True
        if not factor:
            return p
    return "Not found"


def snpf(s):
    if len(s) != 5:
        raise Exception('5 digits only')
    known = {}
    for i in range(5):
        if s[i].isnumeric():
            known[i] = int(s[i])
    return smallest_prime_nonfactor_(candidates(5, known))


assert smallest_prime_nonfactor(30030) == 17
assert smallest_prime_nonfactor_(candidates(5, {0: 3, 1: 0, 2: 0, 3:  3})) == 29
assert snpf('3003?') == 29
