import math
def solution(progresses, speeds):
    answer = []
    day = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    while day:
        baepo = 1
        now = day.pop(0)

        while day and day[0] <= now:
            baepo += 1
            day.pop(0)
        
        answer.append(baepo)

    return answer