import sys

def findSushi(N, d, k, c, l):

    mem = [0]*(d+1)
    low, high = 0, 0
    maxSushi = -1
    cnt = 0

    while(low < N):
        if(mem[l[high%N]] < 1 and cnt != k):
            mem[l[high%N]] += 1
            high += 1
            cnt += 1
        else:
            mem[l[low%N]] -= 1
            low += 1
            cnt -= 1
        if(mem[c] == 0):
            maxSushi = max(maxSushi, high-low+1)
        else:
            maxSushi = max(maxSushi, high-low)
    
    return maxSushi


def solution(N, d, k, c, arr):

    lo, hi, sushies, cnt, ans = 0, k-1, [0]*(d+1), 0, 0
    for s in arr[:k] + [c]:
        if sushies[s] == 0:
            cnt += 1
        sushies[s] += 1

    while lo < N:

        ans = max(ans, cnt)

        sushies[arr[lo]] -= 1
        if sushies[arr[lo]] == 0:
            cnt -= 1
        lo += 1

        hi = (hi + 1) % N
        sushies[arr[hi]] += 1
        if sushies[arr[hi]] == 1:
            cnt += 1

    return ans


if __name__ == "__main__":
    #N, d, k, c = map(int, sys.stdin.readline().split())
    #l = [int(sys.stdin.readline()) for i in range(N)]
    import random
    N, d, k, c = 6, 6, 4, 6

    for _ in range(100000):
        arr = [random.randint(1, d-1) for _ in range(N)]
        if findSushi(N, d, k, c, arr) != solution(N, d, k, c, arr):
            print(N, d, k, c, arr, findSushi(N, d, k, c, arr), solution(N, d, k, c, arr))
            break
