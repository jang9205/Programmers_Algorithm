def solution(board):
    try:
        answer = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i == 0 and j == 0:
                    
                    
                if board[i-1][j-1] == 0 and board[i-1][j] == 0 and board[i-1][j+1] == 0 and board[i][j-1] == 0 and board[i][j+1] == 0 and board[i+1][j-1] and board[i+1][j] == 0 and board[i+1][j+1]:
                    answer += 1
        return answer