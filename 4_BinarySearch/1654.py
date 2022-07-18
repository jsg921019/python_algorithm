# https://www.acmicpc.net/problem/1654

import sys

def solution(K, N, arr):

    def f(l):
        return sum(a//l for a in arr)

    lo, hi = 1, max(arr)

    while lo <= hi:

        mid = (lo + hi) // 2
        val_mid = f(mid)

        if val_mid < N:
            hi = mid - 1
        else:
            lo = mid + 1

    return hi

K, N = map(int,sys.stdin.readline().split())
arr = [*map(int, sys.stdin.readlines())]
print(solution(K, N, arr))