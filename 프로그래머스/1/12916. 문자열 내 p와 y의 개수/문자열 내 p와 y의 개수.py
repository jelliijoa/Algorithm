def solution(s):
    answer = True
    
    s = s.lower()
    p, y = 0, 0
    
    for i in s:
        if i == 'p':
            p += 1
            
        elif i == 'y':
            y += 1
    
    if (p == y) or (p == y == 0):
        return True
    
    else:
        return False