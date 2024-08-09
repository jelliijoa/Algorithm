'''
def solution(k, m, score):
    # 내림차순 정렬 후에 m번째 값(점수)마다 m이랑 곱해서 누적합을 구하면 되는 문제
    score = sorted(score, reverse=True)
    answer = 0
    
    for i in range(m-1, len(score), m):
        answer += score[i] * m
        
    return answer
'''

def solution(k, m, score):
    score = sorted(score, reverse=True)
    return sum(score[i] * m for i in range(m-1, len(score), m))