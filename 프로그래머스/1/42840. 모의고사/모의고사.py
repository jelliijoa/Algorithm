import math

def solution(answers):
    score = [0, 0, 0]
    
    one = [1, 2, 3, 4, 5] * math.ceil(len(answers) / 5)
    two = [2, 1, 2, 3, 2, 4, 2, 5] * math.ceil(len(answers) / 8)
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * math.ceil(len(answers) / 10)
    
    for n, a in zip(one, answers):
        if n == a:
            score[0] += 1
            
    for n, a in zip(two, answers):
        if n == a:
            score[1] += 1
    
    for n, a in zip(three, answers):
        if n == a:
            score[2] += 1
    
    max_score = max(score)

    return [i + 1 for i, s in enumerate(score) if s == max_score]