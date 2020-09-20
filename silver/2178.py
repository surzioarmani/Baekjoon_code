from collections import deque

N, M = map(int, input().split())

mr = [list(map(int,list(input()))) for _ in range(N)]


dx = [0,0,1,-1]
dy = [1,-1,0,0]

go = deque()                          
check = [[False]*M for _ in range(N)] # 한번 갔다온 곳인지 체크
count = [[0]*M for _ in range(N)]      # 카운팅할 배열

go.append((0,0))
check[0][0] = True
count[0][0] = 1

print(mr)
print(check)

while go:
    x, y = go.popleft()  #pop을 통해 있던 곳에서 갈 수 있는 곳 체크
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
                if check[nx][ny] == False and mr[nx][ny] == 1:
                    go.append((nx, ny))
                    count[nx][ny] = count[x][y] + 1
                    check[nx][ny] = True



print(count[N-1][M-1])
                
            
        


