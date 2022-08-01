# https://www.acmicpc.net/problem/1987

import sys

def solution(R, C, grid):
    
    visited = set()
    ans = 0

    def bt(i, j):

        nonlocal ans
        if grid[i][j] in visited:
            ans = max(len(visited), ans)
            return
        
        visited.add(grid[i][j])
        for _i, _j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= _i < R and 0 <= _j < C:
                bt(_i, _j)
        visited.remove(grid[i][j])

    bt(0, 0)
    return ans


R, C = map(int, sys.stdin.readline().split())
grid = [list(row.rstrip()) for row in sys.stdin.readlines()]
print(solution(R, C, grid))