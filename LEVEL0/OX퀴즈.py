def solution(quiz):
    answer = []
    quizlist = []
    for i in quiz:
        quizlist = i.split()
        if quizlist[1] == '+':
            if int(quizlist[0]) + int(quizlist[2]) == int(quizlist[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(quizlist[0]) - int(quizlist[2]) == int(quizlist[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer