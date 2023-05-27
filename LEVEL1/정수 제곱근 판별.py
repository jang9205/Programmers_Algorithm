# 방법 1
def solution(n):
    for i in range(1,n+1):
        if pow(i,2) == n:
            return pow(i+1,2)
    return -1

# 방법 2
def solution(n):
    a = pow(n,1/2)
    if a % 1 == 0:
        return pow(a+1,2)
    return -1