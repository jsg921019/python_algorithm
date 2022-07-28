from collections import deque

def solution(maps):

    dq = deque([(0, 0, 1)])
    N, M = len(maps), len(maps[0])
    
    while dq:
        
        i, j, d = dq.popleft()
        
        if not (0 <= i < N and 0 <= j < M and maps[i][j] == 1):
            continue
        
        if i == N-1 and j == M-1:
            return d
        
        maps[i][j] = 0
        
        dq += [(i+1, j, d+1), (i-1, j, d+1), (i, j+1, d+1), (i, j-1, d+1)]

    return -1