def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if len(board) == 1 and len(board[i]) == 1:
                if board[i][j] == 0:
                    return 1
                
            if i == 0 and j == 0:
                if board[i][j] == 0 and board[i+1][j+1] == 0 and board[i][j+1] == 0 and board[i+1][j] == 0:
                    answer += 1
            elif i == 0 and j == len(board[i]) - 1:
                if board[i][j] == 0 and board[i][j-1] == 0 and board[i+1][j-1] == 0 and board[i+1][j] == 0:
                    answer += 1
            elif i == 0:
                if board[i][j] == 0 and board[i][j-1] == 0 and board[i][j+1] == 0 and board[i+1][j-1] == 0 and board[i+1][j] == 0 and board[i+1][j+1] == 0:
                    answer += 1
            elif i == len(board) - 1 and j == 0:
                if board[i][j] == 0 and board[i-1][j] == 0 and board[i-1][j+1] == 0 and board[i][j+1] == 0:
                    answer += 1
            elif i == len(board) - 1 and j == len(board[i]) - 1:
                if board[i][j] == 0 and board[i-1][j-1] == 0 and board[i-1][j] == 0 and board[i][j-1] == 0:
                    answer += 1
            elif j == 0:
                if board[i][j] == 0 and board[i-1][j] == 0 and board[i-1][j+1] == 0 and board[i][j+1] == 0 and board[i+1][j] == 0 and board[i+1][j+1] == 0:
                    answer += 1
            elif j == len(board[i]) - 1:
                if board[i][j] == 0 and board[i-1][j-1] == 0 and board[i-1][j] == 0 and board[i][j-1] == 0 and board[i+1][j-1] == 0 and board[i+1][j] == 0:
                    answer += 1
            elif i == len(board) - 1:
                if board[i][j] == 0 and board[i-1][j-1] == 0 and board[i-1][j] == 0 and board[i-1][j+1] == 0 and board[i][j-1] == 0 and board[i][j+1] == 0:
                    answer += 1
            else:
                if board[i][j] == 0 and board[i-1][j-1] == 0 and board[i-1][j] == 0 and board[i-1][j+1] == 0 and board[i][j-1] == 0 and board[i][j+1] == 0 and board[i+1][j-1] == 0 and board[i+1][j] == 0 and board[i+1][j+1] == 0:
                    answer += 1
    return answer