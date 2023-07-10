# 풀이1(노가다..)
def solution(dartResult):
    score1, score2, score3 = 0, 0, 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit() and i == 0:
            score1 = int(dartResult[i])
        elif dartResult[i].isdigit() and i == 1:
            score1 = score1 * 10 + int(dartResult[i])
        elif dartResult[i] == 'D' and i == 1:
            score1 = score1 ** 2
        elif dartResult[i] == 'T' and i == 1:
            score1 = score1 ** 3
        elif dartResult[i] == '#' and i == 2:
            score1 = -score1
        elif dartResult[i] == '*' and i == 2:
            score1 *= 2
        
        elif dartResult[i].isdigit() and i >= len(dartResult) - 3 and score3 == 0:
            score3 = int(dartResult[i])
        elif dartResult[i].isdigit() and score3 > 0:
            score3 = score3 * 10 + int(dartResult[i])
        elif dartResult[i] == 'D' and i >= len(dartResult) - 2:
            score3 = score3 ** 2
        elif dartResult[i] == 'T' and i >= len(dartResult) - 2:
            score3 = score3 ** 3
        elif dartResult[i] == '#' and i == len(dartResult) - 1:
            score3 = -score3
        elif dartResult[i] == '*' and i == len(dartResult) - 1:
            score2 *= 2
            score3 *= 2
        
        elif dartResult[i].isdigit() and score2 == 0:
            score2 = int(dartResult[i])
        elif dartResult[i].isdigit() and score2 >= 1:
            score2 = score2 * 10 + int(dartResult[i])
        elif dartResult[i] == 'D':
            score2 = score2 ** 2
        elif dartResult[i] == 'T':
            score2 = score2 ** 3
        elif dartResult[i] == '#':
            score2 = -score2
        elif dartResult[i] == '*':
            score1 *= 2
            score2 *= 2
    return score1 + score2 + score3

# 풀이2
def solution(dartResult):
    dart = {'S':1, 'D':2, 'T':3}
    scores = []
    n = 0

    for i, d in enumerate(dartResult):
        if d in dart:
            scores.append(int(dartResult[n:i]) ** dart[d])
        if d == '*':
            scores[-2:] = [x * 2 for x in scores[-2:]]
        if d == '#':
            scores[-1] = (-1) * scores[-1]
        if not (d.isnumeric()):
            n = i + 1

    return sum(scores)