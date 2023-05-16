# 내 풀이
def solution(bin1, bin2):
    st = int(bin1) + int(bin2)
    st = str(st)
    answer = []
    temp = 0
    for i in range (len(st)-1,-1,-1):
        if st[i] == '0':
            answer.insert(0, str(temp))
            temp = 0
        if st[i] == '1' and temp == 0:
            answer.insert(0, '1')
            temp = 0
        if st[i] == '1' and temp == 1:
            answer.insert(0, '0')
            temp = 1
        if st[i] == '2':
            answer.insert(0, str(temp))
            temp = 1
    if temp == 1:
        answer.insert(0, '1')
    return ''.join(answer)

# 간단한 풀이
def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer