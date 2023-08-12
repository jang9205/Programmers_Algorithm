from collections import Counter

def solution(want, number, discount):
    answer = 0
    wn = {}
    for i in range(len(want)):
        wn[want[i]] = number[i]
    
    for j in range(len(discount) - 9):
        c = Counter(discount[j:j+10])
        if c == wn:
            answer += 1

    return answer