def solution(s):
    queue = list()
    
    if s[0] == ')':
        return False
    
    for b in s:
        if b == '(':
            queue.append(b)
        elif b == ')' and queue:
            queue.pop()
    
    return not queue