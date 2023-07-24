def solution(survey, choices):
    answer = ''
    type_score = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(len(survey)):
        if choices[i] == 1:
            type_score[survey[i][0]] += 3
        elif choices[i] == 2:
            type_score[survey[i][0]] += 2
        elif choices[i] == 3:
            type_score[survey[i][0]] += 1
        elif choices[i] == 4:
            continue
        elif choices[i] == 5:
            type_score[survey[i][1]] += 1
        elif choices[i] == 6:
            type_score[survey[i][1]] += 2
        elif choices[i] == 7:
            type_score[survey[i][1]] += 3

    if type_score['R'] >= type_score['T']:
        answer += 'R'
    else:
        answer += 'T'
    if type_score['C'] >= type_score['F']:
        answer += 'C'
    else:
        answer += 'F'
    if type_score['J'] >= type_score['M']:
        answer += 'J'
    else:
        answer += 'M'
    if type_score['A'] >= type_score['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer