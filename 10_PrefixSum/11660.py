# https://www.acmicpc.net/problem/11660

import sys

def solution(arr, queries):

    arr = [[0]*(len(arr)+1)] + arr
    
    for i in range(1, len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] += arr[i-1][j]
    for j in range(1, len(arr[0])):
        for i in range(len(arr)):
            arr[i][j] += arr[i][j-1]

    for x1, y1, x2, y2 in queries:
        print(arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1])

N, M = map(int, sys.stdin.readline().split())
arr = [[0]+[*map(int, sys.stdin.readline().split())] for _ in range(N)]
queries = [[*map(int, sys.stdin.readline().split())] for _ in range(M)]
solution(arr, queries)