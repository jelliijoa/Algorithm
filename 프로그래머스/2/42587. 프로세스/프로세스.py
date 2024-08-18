from collections import deque

def solution(priorities, location):
    pri = [(i, p) for i, p in enumerate(priorities)]
    queue = deque(pri)
    order = 0
    
    while queue:
        process = queue.popleft()
        
        if any(process[1] < other[1] for other in queue):
            queue.append(process)
        
        else:
            order += 1
            if process[0] == location:
                return order