def solution(my_string):
    temp = 0
    answer = 0
    my_string += ' '
    for i in range (len(my_string)):
        if my_string[i].isdigit():
            temp = temp * 10 + int(my_string[i])
        else:
            answer += temp
            temp = 0
    return answer