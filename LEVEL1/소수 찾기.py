# 방법 1
import math

def solution(n):
    answer = 0
    for i in range(2, n+1):
        for j in range(2, int(math.sqrt(i)+1)):
            if i % j == 0:
                break
        else:
            answer += 1
    return answer

# 방법 2(에라토스테네스의 체)
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)