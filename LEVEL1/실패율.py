def solution(N, stages):
    percent, result = [], []
    for i in range(1, N + 1):
        count = 0
        for j in stages:
            if j >= i:
                count += 1
        percent.append(stages.count(i)/count)
        
    while len(result) < N:
        for k, l in enumerate(percent):
            if l == max(percent):
                result.append(k + 1)
                percent[k] = -1
            if len(result) == N:
                break
    return result