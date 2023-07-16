def solution(s):
    temp = []
    for i in s:
        temp.append(i)
        if len(temp) > 1 and temp[-1] == temp[-2]:
            temp.pop()
            temp.pop()
    if temp == []:
        return 1
    return 0