def solution(my_string):
    answer = 0
    for i in ['1','2','3','4','5','6','7','8','9']:
        answer += my_string.count(i) * int(i)
    return answer