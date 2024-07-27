def solution(nums):
    n = len(set(nums))
    return min(len(nums)/2, n)