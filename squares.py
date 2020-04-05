import math


def up_to(limit):
    root = int(math.floor(math.sqrt(limit)))
    return [n * n for n in range(1, root+1)]


