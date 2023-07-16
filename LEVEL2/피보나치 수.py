def solution(n):
    f_x0, f_x1 = 0, 1
    count = 1
    while n != count:
        f_x2 = f_x0 + f_x1
        count += 1
        if n == count:
            return f_x2 % 1234567
        f_x0 = f_x1 + f_x2
        count += 1
        if n == count:
            return f_x0 % 1234567
        f_x1 = f_x2 + f_x0
        count += 1
    return f_x1 % 1234567