def solution(sides):
    answer = 0
    sides.sort()
    for i in range (1,2000):
        if sides[1] >= i and sides[1] < i + sides[0]:
            answer += 1
        elif sides[1] < i and i < sides[0] + sides[1]:
            answer += 1
    return answer