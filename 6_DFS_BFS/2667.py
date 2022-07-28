# https://www.acmicpc.net/problem/2667

import sys

def solution(N, grid):    

    def dfs(i_s, j_s):
        cnt = 0
        s = [(i_s, j_s)]
        grid[i_s][j_s] = 0
        
        while s:
            i, j = s.pop()
            cnt += 1
            
            for _i, _j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= _i < N and 0 <= _j < N and grid[_i][_j] == 1:
                    grid[_i][_j] = 0
                    s.append((_i, _j))
                    
        return cnt
    
    cnts = []

    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                cnts.append(dfs(i, j))
    
    return [len(cnts)] + sorted(cnts)

N = int(sys.stdin.readline())
grid = [[*map(int, row.rstrip())] for row in sys.stdin.readlines()]
print(*solution(N, grid), sep='\n')