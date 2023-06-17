def solution(s):
    answer, temp = [], []
    for i in range(len(s)):
        temp = s[:i+1]
        if temp.count(temp[-1]) > 1:
            count = 1
            for j in range(len(temp) - 2, -1, -1):
                if temp[j] != temp[-1]:
                    count += 1
                else:
                    answer.append(count)
                    break
        else:
            answer.append(-1)
    return answer