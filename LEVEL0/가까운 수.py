def solution(array, n):
    array.sort()
    answer = 0
    ab = 100
    for i in array:
        if abs(n-i) < ab:
            ab = abs(n-i)
            answer = i
    return answer