# 내 풀이
def solution(numbers, k):
    answer = 0
    for i in range (k-1):
        if answer < len(numbers) - 2:
            answer += 2
        elif answer == len(numbers) - 2:
            answer = 0
        elif answer == len(numbers) - 1:
            answer = 1
    return numbers[answer]

# 간단한 풀이..
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]