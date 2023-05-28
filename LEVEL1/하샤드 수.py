def solution(x):
    n, temp = 0, x
    while x > 0:
        n += x % 10
        x = x // 10
    if temp % n == 0:
        return True
    return False