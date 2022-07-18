from collections import Counter
from re import findall

def solution(s):
    
    nums = []
    num = ""
    
    for c in s:
        if c.isdigit():
            num += c
        else:
            if num:
                nums.append(int(num))
                num = ""
                
    cntr = {}
    for num in nums:
        if num in cntr:
            cntr[num] += 1
        else:
            cntr[num] = 1
            
    answer = sorted(cntr.keys(), key=lambda x: cntr[x], reverse=True)
    
    return answer


def solution(s):
    
    for c in '{},':
        s = s.replace(c, ' ')
    
    nums = [int(n) for n in s.split()]
                
    cntr = Counter(nums)
            
    answer = sorted(cntr.keys(), key=lambda x: cntr[x], reverse=True)
    
    return answer


def solution(s):
    return [int(c) for c, _ in Counter(findall('\d+', s)).most_common()]