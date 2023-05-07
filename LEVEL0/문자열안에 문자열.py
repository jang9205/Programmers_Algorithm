# 방법1
def solution(str1, str2):
    for i in range (0,len(str1)):
        if str1[i:i + len(str2)] == str2:
            return 1
    return 2

# in 쓰면 간단..
def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2
    
# count도 가능
def solution(str1, str2):
    if str1.count(str2):
        return 1
    else:
        return 2