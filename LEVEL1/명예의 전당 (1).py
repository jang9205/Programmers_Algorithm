def solution(k, score):
    temp, result = [], []
    for i in score:
        if len(temp) < k:
            temp.append(i)
        elif len(temp) >= k and i >= min(temp):
            temp.remove(min(temp))
            temp.append(i)
        result.append(min(temp))
    return result