# 방법 1
def solution(n):
    answer, j = 0, 0
    for i in range(1,n+1):
        j = n // i
        if i * j == n:
            answer += 1
    return answer

# 방법 2
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += 1
    return answer