def up_to(limit):
    result = []
    n = inc = 1
    while n <= limit:
        result.append(n)
        inc += 1
        n += inc
    return result
