# https://www.acmicpc.net/problem/20207

import sys

def solution(arr):
    
    def get_area(paper_start, paper_ends):
        return len(paper_ends) * (max(paper_ends) - paper_start + 1)

    arr.sort(key=lambda x:(x[0], -x[1]))

    ans = 0
    paper_start, paper_ends = 1, [0]

    for start, end in arr:

        if start > max(paper_ends)+1:
            ans += get_area(paper_start, paper_ends)
            paper_start, paper_ends = start, [end]

        else:
            for i, paper_end in enumerate(paper_ends):
                if start > paper_end:
                    paper_ends[i] = end
                    break
            else:
                paper_ends.append(end)
    
    return ans + get_area(paper_start, paper_ends)

N = sys.stdin.readline()
arr = [[*map(int, row.split())] for row in sys.stdin.readlines()]
print(solution(arr))