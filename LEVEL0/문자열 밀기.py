# 내 풀이
def solution(A, B):
    count = 0
    A1 = ''
    if A == B:
        return 0
    while True:
        if A1 == B:
            break
        count += 1
        A1 = A[-1]
        A1 += A[:-1]
        A = A1
        if count > len(A):
            return -1
    return count

# 간단한 풀이..
def solution(A, B):
    return (B * 2).find(A)