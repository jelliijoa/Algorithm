import sys
from collections import defaultdict, deque

input = sys.stdin.read

def solve():
    data = input().split()
    N = int(data[0])
    C = int(data[1])
    
    tree = defaultdict(list)
    distances = [0] * (N + 1)
    
    index = 2
    for _ in range(C):
        E_i = int(data[index])
        B1_i = int(data[index + 1])
        B2_i = int(data[index + 2])
        tree[E_i].append(B1_i)
        tree[E_i].append(B2_i)
        index += 3
    
    queue = deque([1])
    distances[1] = 1
    
    while queue:
        current = queue.popleft()
        for neighbor in tree[current]:
            if distances[neighbor] == 0:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    for i in range(1, N + 1):
        print(distances[i])

solve()