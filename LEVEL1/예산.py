def solution(d, budget):
    count = 0
    d.sort()
    for i in d:
        if budget >= i:
            budget -= i
            count += 1
    return count