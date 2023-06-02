def solution(s):
    for i in s:
        if i.isalpha() == True:
            return False
    if len(s) == 4 or len(s) == 6:
        return True 
    return False