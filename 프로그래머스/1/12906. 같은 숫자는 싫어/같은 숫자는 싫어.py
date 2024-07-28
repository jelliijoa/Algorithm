def solution(arr):
    result = []
    for n in arr:
        if len(result) == 0 or result[-1] != n:
            result.append(n)
    return result