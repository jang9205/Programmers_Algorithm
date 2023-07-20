# 풀이 1
import math
def solution(n,a,b):
    answer = 0
    while True:
        answer += 1
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        if a == b or a == 0 or b == 0:
            break
    return answer

# 풀이 2
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2
    return answer