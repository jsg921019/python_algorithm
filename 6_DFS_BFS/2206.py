# https://www.acmicpc.net/problem/2206

import sys
from collections import deque

def solution(N, M, grid):

    q = deque([(0, 0, False, 1)])
    visited = set([(0, 0, False)])

    while q:

        i, j, k, d = q.popleft()

        if i == N-1 and j == M-1:
            return d

        if k:
            for _i, _j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= _i < N and 0 <= _j < M and grid[_i][_j] == 0 and (_i, _j, k) not in visited:
                    visited.add((_i, _j, k))
                    q.append((_i, _j, k, d+1))

        else:
            for _i, _j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= _i < N and 0 <= _j < M and grid[_i][_j] == 0 and (_i, _j, k) not in visited:
                    visited.add((_i, _j, k))
                    q.append((_i, _j, k, d+1))

                elif 0 <= _i < N and 0 <= _j < M and grid[_i][_j] == 1 and (_i, _j, True) not in visited:
                    visited.add((_i, _j, True))
                    q.append((_i, _j, True, d+1))

    return -1

N, M = map(int, sys.stdin.readline().split())
grid = [[*map(int, row.rstrip())] for row in sys.stdin.readlines()]
print(solution(N, M, grid))