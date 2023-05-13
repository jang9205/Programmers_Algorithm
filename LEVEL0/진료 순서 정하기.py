def solution(emergency):
    answer = []
    for i in emergency:
        count = 0
        for j in emergency:
            if i <= j:
                count += 1
        answer.append(count)
    return answer