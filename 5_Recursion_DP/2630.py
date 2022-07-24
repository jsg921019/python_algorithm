# https://www.acmicpc.net/problem/2630

import sys

def solutionRec(N, paper):

    def f(i, j, N):

        if N == 1:
            return 1 - paper[i][j], paper[i][j]

        splits = [f(i, j, N//2), f(i+N//2, j, N//2), f(i, j+N//2, N//2), f(i+N//2, j+N//2, N//2)]
        whites, blues = sum(sp[0] for sp in splits), sum(sp[1] for sp in splits)

        if whites == 0:
            return 0, 1
        if blues == 0:
            return 1, 0
        return whites, blues

    return f(0, 0, N)

N = int(sys.stdin.readline())
paper = [[*map(int, row.split())] for row in sys.stdin.readlines()]
print(*solutionRec(N, paper), sep='\n')


# https://www.acmicpc.net/problem/2630

import sys

def solutionDP(N, paper):

    def combine(i, j):
        white = dp[i][j][0] + dp[i][j+1][0] + dp[i+1][j][0] + dp[i+1][j+1][0]
        blue = dp[i][j][1] + dp[i][j+1][1] + dp[i+1][j][1] + dp[i+1][j+1][1]
        if white == 0:
            return 0, 1
        if blue == 0:
            return 1, 0
        return white, blue

    dp = [[(1-paper[i][j], paper[i][j]) for j in range(N)] for i in range(N)]

    while N > 1:
        dp = [[combine(i, j) for j in range(0, N, 2)] for i in range(0, N, 2)]
        N //= 2
        
    return dp[0][0]

N = int(sys.stdin.readline())
paper = [[*map(int, row.split())] for row in sys.stdin.readlines()]
print(*solutionDP(N, paper), sep='\n')