def solution(N, stages):
    percent, result = [], []
    for i in range(1, N + 1):
        count = 0
        for j in stages:
            if j >= i:
                count += 1
        if count != 0:
            percent.append(stages.count(i) / count)
        else:
            percent.append(0)
    
    for k in range(len(percent)):
        result.append(percent.index(max(percent)) + 1)
        percent[percent.index(max(percent))] = -1
    return result