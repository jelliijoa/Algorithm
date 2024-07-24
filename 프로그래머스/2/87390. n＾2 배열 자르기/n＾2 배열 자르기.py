def solution(n, left, right):
    result = []
    for k in range(left, right + 1):
        i = k // n
        j = k % n
        result.append(max(i, j) + 1)
    return result