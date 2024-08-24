from collections import deque

def bfs(start, graph, visited, H, W):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < H and 0 <= ny < W:
                if graph[nx][ny] == '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def count_sheep(H, W, graph):
    visited = [[False] * W for _ in range(H)]
    count = 0
    
    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#' and not visited[i][j]:
                bfs((i, j), graph, visited, H, W)
                count += 1
    
    return count

T = int(input())

for _ in range(T):
    H, W = map(int, input().split())
    graph = [list(input().strip()) for _ in range(H)]
    
    result = count_sheep(H, W, graph)
    print(result)
