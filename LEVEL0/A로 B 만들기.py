# 처음 풀이
def solution(before, after):
    before = sorted(before)
    after = sorted(after)
    for i in range (len(before)):
        if before[i] != after[i]:
            return 0
    return 1

# 반복문 왜썼지..
def solution(before, after):
    before = sorted(before)
    after = sorted(after)
    if before != after:
        return 0
    return 1
