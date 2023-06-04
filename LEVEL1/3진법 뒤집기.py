# 풀이 1
def solution(n):
    answer = 0
    temp = ''
    while n > 0:
        temp += str(n % 3)
        n = n // 3
    le = len(temp) - 1
    for i in temp:
        answer += int(i) * (3 ** le)
        le -= 1
    return answer

# 풀이 2
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer