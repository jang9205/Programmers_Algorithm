def solution(my_string):
    my_string = list(my_string)
    for i in range (len(my_string)-1,0,-1):
        for j in range (i-1,-1,-1):
            if my_string[i] == my_string[j]:
                my_string.pop(i)
                break
    return ''.join(my_string)