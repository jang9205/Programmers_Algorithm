# 내장함수사용
def solution(my_string):
    answer = 0
    my_string = list(my_string)
    my_string.reverse()
    answer = ''.join(my_string)
    return answer

# 간단한 풀이
def solution(my_string):
    return my_string[::-1]