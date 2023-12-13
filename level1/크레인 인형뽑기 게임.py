def solution(board, moves):
    pick = [""]
    cnt = 0
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                pick.append(board[j][i-1])
                board[j][i-1] = 0
                
                if pick[-1] == pick[-2]:
                    cnt += 2
                    pick.pop()
                    pick.pop()
                break
                
    return cnt