# https://www.acmicpc.net/problem/1548

import sys

def solution(N, nums):
    nums.sort()
    for n in range(N, 0, -1):
        for i in range(N - n + 1):
            if n < 3 or nums[i] + nums[i+1] > nums[i+n-1]:
                return n
            
N = int(sys.stdin.readline())
nums = [int(n) for n in sys.stdin.readline().split()]
print(solution(N, nums))