import math

def findLcm(x, y):
    return abs(x * y) // math.gcd(x, y)

nums = list(map(int, input().split()))
answer = float('inf')

for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            cur = findLcm(findLcm(nums[i], nums[j]), nums[k])
            if cur < answer:
                answer = cur

print(answer)