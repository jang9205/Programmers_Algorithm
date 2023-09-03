def solution(s, skip, index):
    answer = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    for i in skip:
        if i in alpha:
            alpha = alpha.replace(i, "")
    
    for j in s:
        temp = alpha[(alpha.index(j) + index) % len(alpha)]
        answer += temp
    
    return answer