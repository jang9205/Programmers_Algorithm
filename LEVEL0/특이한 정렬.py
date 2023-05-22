# 풀이 1
def solution(numlist, n):
    answer = []
    numlist.sort()
    num = len(numlist)
    while len(answer) < num:
        ab = 10000
        temp = 0
        for i in numlist:
            if abs(i - n) <= ab:
                ab = abs(i - n)
                temp = i
        numlist.remove(temp)
        answer.append(temp)
    return answer

# 풀이 2
def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer