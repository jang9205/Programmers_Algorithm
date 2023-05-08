def solution(my_string):
    answer = ''
    for i in my_string:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            answer += i.upper()
        else:
            answer += i.lower()
    return answer