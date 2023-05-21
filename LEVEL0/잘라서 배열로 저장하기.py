def solution(my_str, n):
    answer = []
    k = 0
    for i in range (1,len(my_str)//n+1):
        answer.append(my_str[k:i*n])
        k += n
    if len(my_str) % n > 0:
        answer.append(my_str[k:])
    return answer