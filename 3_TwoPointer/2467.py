# https://www.acmicpc.net/problem/2467

import sys

def solution(N, arr):

    lo, hi, ans_tot, ans_lo, ans_hi = 0, N - 1, float('inf'), 0, N - 1

    while lo < hi:

        tot = arr[lo] + arr[hi]
        if abs(tot) < ans_tot:
            ans_tot, ans_lo, ans_hi = abs(tot), lo, hi

        if tot > 0:
            hi -= 1
        elif tot < 0:
            lo += 1
        else:
            break

    return arr[ans_lo], arr[ans_hi]

N = int(sys.stdin.readline())
arr = [*map(int, sys.stdin.readline().split())]
print(*solution(N,arr))