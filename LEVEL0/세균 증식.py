# 방법 1
def solution(n, t):
    for i in range (t):
        n = n * 2
    return  n

#방법 2
def solution(n, t):
    return n*(2**t)