# 리스트 삭제
def solution(numbers, num1, num2):
    del numbers[num2 + 1:]
    del numbers[:num1]
    return numbers

# 리스트 슬라이싱
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]