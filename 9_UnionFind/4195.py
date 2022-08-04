# https://www.acmicpc.net/problem/4195

import sys

def find(a, parents, nums):
    while a in parents:
        a = parents[a]
    return a, nums.get(a, 1)

def union(a, b, parents, nums):
    p_a, n_a = find(a, parents, nums)
    p_b, n_b = find(b, parents, nums)
    if p_a > p_b:
        parents[p_a] = p_b
        nums[p_b] = n_a + n_b
        return nums[p_b]
    elif p_b > p_a:
        parents[p_b] = p_a
        nums[p_a] = n_a + n_b
        return nums[p_a]
    else:
        return n_a
    
def solution(queries):

    parents = {}
    nums = {}

    for a, b in queries:
        print(union(a, b, parents, nums))

for _ in range(int(sys.stdin.readline())):
    queries = [sys.stdin.readline().split() for _ in range(int(sys.stdin.readline()))]
    solution(queries)