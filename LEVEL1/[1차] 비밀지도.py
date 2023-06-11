# 풀이 1
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = ''
        bi = int(format(arr1[i], 'b')) + int(format(arr2[i], 'b'))
        bi = '00000' + str(bi)
        for j in range(-n,0):
            if bi[j] == '0':
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
    return answer

# 풀이 2
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = bin(arr1[i]|arr2[i])[2:].rjust(n,'0').replace('1','#').replace('0',' ')
        answer.append(a)
    return answer