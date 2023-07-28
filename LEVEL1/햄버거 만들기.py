def solution(ingredient):
    answer, i = 0, 0
    while i < len(ingredient) - 3:
        if ingredient[i:i+4] == [1, 2, 3, 1]:
            answer += 1
            del ingredient[i:i+4]
            i -= 3
        i += 1
    return answer