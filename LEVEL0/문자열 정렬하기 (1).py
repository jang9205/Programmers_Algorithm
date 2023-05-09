# 방법 1
def solution(my_string):
    answer = []
    for i in range (len(my_string)):
        if ord(my_string[i]) >= ord('0') and ord(my_string[i]) <= ord('9'):
            answer.append(int(my_string[i]))
    answer.sort()
    return answer

# 방법 2
def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    answer.sort()
    return answer