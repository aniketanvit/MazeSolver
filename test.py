def heuristic ():
    pass


def euclidean (a, b, c, d):
    xd = a - c
    yd = b - d
    return (xd * xd) + (yd * yd)


def manhattan (a, b, c, d):
    return abs (a - c) + abs (b - d)


def test (function, a, b, c, d):
    print function (a, b, c, d)


if __name__ == '__main__':
    test (euclidean, 1, 2, 3, 4)
