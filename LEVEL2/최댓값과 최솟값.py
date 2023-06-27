def solution(s):
    s1 = []
    s = s.split(' ')
    for i in s:
        s1.append(int(i))
    return str(min(s1)) + ' ' + str(max(s1))