def solution(s):
    answer = ''
    for i in range(len(s)):
        if i == 0 and s[i].isalpha():
            answer += s[i].upper()
        elif s[i - 1] == ' ' and s[i].isalpha():
            answer += s[i].upper()
        elif s[i].isalpha():
            answer += s[i].lower()
        else:
            answer += s[i]
    return answer