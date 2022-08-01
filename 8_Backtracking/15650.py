# https://www.acmicpc.net/problem/15650

import sys

def solution(N, M):
    
    path = [0]

    def bt():

        if len(path) == M+1:
            print(*path[1:])
            return

        for i in range(path[-1]+1, N+1):
            path.append(i)
            bt()
            path.pop()

    bt()


N, M = map(int, sys.stdin.readline().split())
solution(N, M)