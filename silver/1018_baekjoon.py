
def solution(ch):
    white = 0
    for i in range(8):
        for j in range(8):
            i_ = ( 0 if i in [0,2,4,6] else 1)
            j_ = ( 0 if j in [0,2,4,6] else 1)
            if (i_ == 0 and j_ == 0) or (i_ == 1 and j_ == 1):
                if ch[i][j] != 'W':
                    white += 1
            if (i_ == 1 and j_ == 0) or (i_ == 0 and j_ == 1):
                if ch[i][j] != 'B':
                    white += 1
                    

    black = 0
    for i in range(8):
       for j in range(8):
           i_ = ( 0 if i in [0,2,4,6] else 1)
           j_ = ( 0 if j in [0,2,4,6] else 1)
           if (i_ == 0 and j_ == 0) or (i_ == 1 and j_ == 1):
               if ch[i][j] != 'B':
                   black += 1
                    
           if (i_ == 1 and j_ == 0) or (i_ == 0 and j_ == 1):
               if ch[i][j] != 'W':
                   black += 1
                               
    return min(black, white)


N, M = map(int, input().split())
board = [list(input()) for i in range(N)]
check = list()

for i in range(N-7):
    for j in range(M-7):
        ch = [a[(0+j):(8+j)] for a in board[(0+i):(8+i)]]
        check.append(solution(ch))

print(min(check))

    



    
    
