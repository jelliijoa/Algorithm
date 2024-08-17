def solution(park, routes):
    directions = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}

    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x, y = i, j

    for route in routes:
        dir, steps = route.split()
        dx, dy = directions[dir]

        nx, ny = x, y
        valid = True
        
        for _ in range(int(steps)):
            nx += dx
            ny += dy
            if not (0 <= nx < len(park) and 0 <= ny < len(park[0])) or park[nx][ny] == 'X':
                valid = False
                break

        if valid:
            x, y = nx, ny

    return [x, y]