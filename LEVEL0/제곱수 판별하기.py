def solution(n):
    for i in range(n+1):
        if pow(i,2) == n:
            return 1
    return 2