def resp(*args):
    result = 0
    for r in args:
        result += 1 / r
    return 1 / result

# print(resp(2, 2, 2, 2))
