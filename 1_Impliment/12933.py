# https://www.acmicpc.net/problem/12933

def solution():

    cntr = {c:0 for c in 'quack'}
    prev = {x:y for x, y in zip('uack', 'quac')}
    ans = 0
    concurrent = 0

    for c in input():
        cntr[c] += 1
        if c == 'q':
            concurrent += 1
            ans = max(ans, concurrent)
        else:
            if not cntr[prev[c]]:
                return -1
            cntr[prev[c]] -= 1
            if c == 'k':
                concurrent -= 1

    return -1 if concurrent else ans

print(solution())