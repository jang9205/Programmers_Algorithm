def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            x = 0
            for k in range(len(arr1[0])):
                x += arr1[i][k] * arr2[k][j]
            row.append(x)
        answer.append(row)
    return answer