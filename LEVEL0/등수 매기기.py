def solution(score):
    avg = []
    answer = []
    for i in score:
        avg.append(i[0] + i[1])
    for j in avg:
        count = 1
        for k in avg:
            if j < k:
                count += 1
        answer.append(count)
    return answer