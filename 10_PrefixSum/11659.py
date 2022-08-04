# https://www.acmicpc.net/problem/11659

import sys
from itertools import accumulate

def solution(arr, queries):
    acc_arr = list(accumulate(arr, initial=0))
    for i, j in queries:
        print(acc_arr[j] - acc_arr[i-1])

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
solution(arr, queries)