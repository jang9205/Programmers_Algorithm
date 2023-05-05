# 처음 풀이
def solution(slice, n):
    for i in range (1,51):
        if slice * i / n >= 1:
            return i

# 다시 풀어보니까 반복문은 오바였다..
def solution(slice, n):
    answer = n // slice + 1
    if n % slice == 0:
        answer -= 1
    return answer