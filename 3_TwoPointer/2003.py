# https://www.acmicpc.net/problem/2003

# import sys
# from itertools import combinations

# N, M = map(int, sys.stdin.readline().split())
# arr = [*map(int, sys.stdin.readline().split())]

# ans = 0
# for i, j in combinations(range(0, N+1), 2):
#     if sum(arr[i:j]) == M:
#         ans += 1

# print(ans)

import sys

def solution(N, M, arr):
    lo, hi, m, ans = 0, 0, arr[0], 0

    while 1:

        if m < M:
            hi += 1
            if hi == N:
                break
            m += arr[hi]

        elif m > M:
            m -= arr[lo]
            lo += 1

        else:
            ans += 1
            m -= arr[lo]
            lo += 1

    return ans

N, M = map(int, sys.stdin.readline().split())
arr = [*map(int, sys.stdin.readline().split())]
print(solution(N, M, arr))