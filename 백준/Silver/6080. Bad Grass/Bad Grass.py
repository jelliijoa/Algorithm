def dfs(grid, i, j, visited, R, C):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    stack = [(i, j)]
    visited[i][j] = True
    
    while stack:
        x, y = stack.pop()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and grid[nx][ny] > 0:
                visited[nx][ny] = True
                stack.append((nx, ny))

def count_islands(grid):
    if not grid:
        return 0
    
    R, C = len(grid), len(grid[0])
    visited = [[False] * C for _ in range(R)]
    island_count = 0
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] > 0 and not visited[i][j]:
                dfs(grid, i, j, visited, R, C)
                island_count += 1
    
    return island_count

R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

print(count_islands(grid))