def solution(n):
    answer = '수박'
    if n % 2 == 0:
        return answer * (n // 2)
    answer = answer * (n // 2 + 1)
    return answer[:-1]