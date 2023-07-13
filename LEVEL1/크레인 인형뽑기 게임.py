def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        for i in board:
            if i[move-1] != 0:
                bucket.append(i[move-1])
                i[move-1] = 0
                if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
                    answer += 2
                    bucket.pop()
                    bucket.pop()
                break
    return answer