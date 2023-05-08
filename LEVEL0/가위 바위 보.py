def solution(rsp):
    answer = []
    for i in range (0,len(rsp)):
        if rsp[i] == '2':
            answer.append('0')
        elif rsp[i] == '0':
            answer.append('5')
        else:
            answer.append('2')  
    return ''.join(answer)

# 리스트를 왜 썼을까..
def solution(rsp):
    answer = ''
    for i in range (0,len(rsp)):
        if rsp[i] == '2':
            answer += '0'
        elif rsp[i] == '0':
            answer += '5'
        else:
            answer += '2' 
    return answer