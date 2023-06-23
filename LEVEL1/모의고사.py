# 풀이 1
def solution(answers):
    answer = []
    su1 = [1, 2, 3, 4, 5]
    su2 = [2, 1, 2, 3, 2, 4, 2, 5]
    su3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count1, count2, count3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == su1[i % 5]:
            count1 += 1
        if answers[i] == su2[i % 8]:
            count2 += 1
        if answers[i] == su3[i % 10]:
            count3 += 1
    if count1 > count2 and count1 > count3:
        return [1]
    elif count2 > count1 and count2 > count3:
        return [2]
    elif count3 > count1 and count3 > count2:
        return [3]
    elif count1 == count2 and count1 != count3:
        return [1, 2]
    elif count2 == count3 and count1 != count2:
        return [2, 3]
    elif count1 == count3 and count2 != count3:
        return [1, 3]
    else:
        return [1, 2, 3]
    
# 풀이 2
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result