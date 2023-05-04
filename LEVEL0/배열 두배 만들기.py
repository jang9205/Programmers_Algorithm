def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i * 2)
    return answer

# 리스트 컴프리헨션: [표현식 for 항목 in 반복가능객체 if 조건문]
def solution(numbers):
    return [num*2 for num in numbers]