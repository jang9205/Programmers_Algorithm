def solution(n):
    global answer
    answer = []
    hanoi(n, 1, 2, 3)
    return answer

def hanoi(n, st, mid, end):
    if n == 1:
        answer.append([st, end])
        return
    hanoi(n-1, st, end, mid)
    hanoi(1, st, mid, end)
    hanoi(n-1, mid, st, end)