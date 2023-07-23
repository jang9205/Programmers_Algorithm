def solution(s):
    answer = 0
    for i in range(len(s)-1):
        temp = s
        for j in range(len(s)//2):
            if '[]' in s:
                s = s.replace('[]', '')
            elif '()' in s:
                s = s.replace('()', '')
            elif '{}' in s:
                s = s.replace('{}', '')
        if s == '':
            answer += 1
        s = temp[1:] + temp[0]
    return answer