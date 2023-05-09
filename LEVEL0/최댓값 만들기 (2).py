# 첫 번째 풀이
def solution(numbers):
    i, answer = 0, []
    for j in range (i,len(numbers)):
        for k in range (i+1,len(numbers)):
            answer.append(numbers[j] * numbers[k])
        i += 1
    answer.sort()
    return answer[-1]

# 두 번째 풀이
def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])

