# https://www.acmicpc.net/problem/15649

import sys

def solution(N, M):

    path = []
    
    def bt():

        if len(path) == M:
            print(*path)

        for i in range(1, N+1):
            if i not in path:
                path.append(i)
                bt()
                path.pop()

    bt() 
    
N, M = map(int, sys.stdin.readline().split())
solution(N, M)