import sys
T = int(input())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    answer = 0
    for a in range(1, n-1):
        for b in range(a+1, n):
            if (a**2 + b**2 + m) % (a*b) == 0:
                answer += 1
    print(answer)