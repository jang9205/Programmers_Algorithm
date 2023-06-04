#방법 1
def solution(n, m):
    a, b = 0, 0
    for i in range(1, max(n,m)+1):
        if n % i == 0 and m % i == 0:
            a = i
    for j in range(max(n,m),99999999999 ,max(n,m)):
        if j % n == 0 and j % m == 0:
            b = j
            break
    return a, b

# 방법 2
import math

def solution(n, m):
    g = math.gcd(n,m)
    l = (n*m)//g
    return [g,l]