def solution(k, tangerine):
    dic = {}
    count = 0
    
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    values = sorted((value for value in dic.values()), reverse = True)
    
    for result, j in enumerate(values):
        count += j
        if count >= k:
            return result + 1