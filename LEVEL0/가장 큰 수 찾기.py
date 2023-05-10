# 첫 번째 풀이
def solution(array):
    answer = [0]
    for i in array:
        if i > answer[0]:
            answer[0] = i
    answer.append(array.index(answer[0]))
    return answer

# 두 번째 풀이
def solution(array):
    ma = max(array)
    return [ma,array.index(ma)]