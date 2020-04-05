import digit


def up_to(limit):
    return [n for n in range(1, limit) if n % digit.sum(n) == 0]
