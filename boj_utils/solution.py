# https://www.acmicpc.net/problem/1253

import sys
import bisect

def solution(N, arr):

    if N < 3:
        return 0

    arr.sort()
    pool = set()
    flag = 0 in arr
    ans = 0

    for i, n in enumerate(arr[1:], 1):
        if n in pool or (flag and i < N-1 and arr[i] == arr[i+1]):
            ans += 1
        for m in arr[:i]:
            pool.add(n+m)
    
    if arr[0] == arr[1] == arr[2]:
        ans += 1

    return ans

     
N = int(sys.stdin.readline())
arr = [*map(int, sys.stdin.readline().split())]
print(solution(N, arr))