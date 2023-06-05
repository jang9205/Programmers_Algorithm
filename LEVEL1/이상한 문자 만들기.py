def solution(s):
    answer = ''
    count = 1
    for i in s:
        if count % 2 == 1 and i != ' ':
            answer += i.upper()
            count += 1
        elif count % 2 == 0 and i != ' ':
            answer += i.lower()
            count += 1
        elif i == ' ':
            answer += ' '
            count = 1
    return answer