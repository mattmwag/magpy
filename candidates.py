from itertools import product


def candidates(digits=1, known_digits={}):
    """Given a number of d digits, and a dict of known_digits,
    return a list of all possibilities for that number."""
    cs = []
    # step through the digits starting with most significant
    for d in range(digits)[::-1]:
        # exponent = 0 for final digit, 1 for penultimate digit, &c
        x = digits - 1 - d
        if d in known_digits.keys():
            addend = known_digits[d] * 10**x
            if not cs:
                # this number is the only current candidate
                cs.append(addend)
            else:
                # add this number to all current candidates
                cs = list(map(lambda c: c + addend, cs))
        else:
            # we have ten options for the current digit
            addends = [n * 10**x for n in range(10)]
            if not cs:
                # these ten numbers are candidates
                cs = list(addends)
            else:
                # add each of these 10 numbers of all existing candidates
                cs = list(map(sum, product(addends, cs)))
    return cs
