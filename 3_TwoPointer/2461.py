# https://www.acmicpc.net/problem/2461

import sys
from heapq import heapify, heappush, heappop

def solution(N, M, arr):

    hq = [(arr[i][0], i, 0) for i in range(N)]
    max_val = max(hq)[0]
    ans = float('inf')
    heapify(hq)
    
    while 1:
        min_val, i, j = heappop(hq)
        ans = min(ans, max_val - min_val)
        if j == M - 1:
            break
        max_val = max(arr[i][j+1], max_val)
        heappush(hq, (arr[i][j+1], i, j+1))

    return ans

N, M = map(int, sys.stdin.readline().split())
arr = [sorted([*map(int, row.split())]) for row in sys.stdin.readlines()]
print(solution(N, M ,arr))