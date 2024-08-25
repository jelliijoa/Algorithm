import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    global count
    visited[x][y] = True
    count += 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] == 0:
            dfs(nx, ny)

M, N, K = map(int, input().split())
grid = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = 1

areas = []

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0 and not visited[i][j]:
            count = 0
            dfs(i, j)
            areas.append(count)

areas.sort()
print(len(areas))
print(' '.join(map(str, areas)))