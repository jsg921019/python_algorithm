# https://www.acmicpc.net/problem/1520

import sys
sys.setrecursionlimit(10000000)
from functools import cache

def solution(M, N, grid):

    @cache
    def rec(i, j):

        if i == 0 and j == 0:
            return 1

        paths = 0
        for _i, _j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= _i < M and 0 <= _j < N and grid[_i][_j] > grid[i][j]:
                paths += rec(_i, _j)
        return paths

    return rec(M-1, N-1)
        
M, N = map(int, sys.stdin.readline().split())
grid = [[*map(int, row.split())] for row in sys.stdin.readlines()]
print(solution(M, N, grid))


# https://www.acmicpc.net/problem/1520

import sys

def solution(M, N, grid):

    dp = [[0]*N for _ in range(M)]
    dp[0][0] = 1

    coors = [(grid[i][j], i, j) for i in range(M) for j in range(N) if grid[i][j] < grid[0][0]]
    coors.sort(reverse=True)

    for v, i, j in coors:
        
        for _i, _j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= _i < M and 0 <= _j < N and grid[_i][_j] > v:
                dp[i][j] += dp[_i][_j]

        if i == M-1 and j == N-1:
            break
            
    return dp[-1][-1]
        
M, N = map(int, sys.stdin.readline().split())
grid = [[*map(int, row.split())] for row in sys.stdin.readlines()]
print(solution(M, N, grid))