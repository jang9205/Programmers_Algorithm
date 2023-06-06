def solution(s, n):
    temp = ''
    answer = s
    for i in range(n):
        for j in answer:
            if j == ' ':
                temp += ' '
            elif j == 'z':
                temp += 'a'
            elif j == 'Z':
                temp += 'A'
            else:
                temp += chr(ord(j) + 1)
        answer = temp
        temp = ''
    return answer