def solution(k, m, score):
    answer = 0
    score = sorted(score)
    for i in range(len(score) // m):
        temp = 0
        for k in range(m):
            temp = score.pop() * m
        answer += temp
    return answer