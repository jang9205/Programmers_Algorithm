def solution(brown, yellow):
    for y in range(1, brown+yellow):
        if (brown + yellow) % y != 0:
            continue
        for x in range(1, brown+yellow):
            if (brown + yellow) % x != 0:
                continue
            if x * y == brown + yellow and (x - 2) * (y - 2) == yellow:
                return x, y