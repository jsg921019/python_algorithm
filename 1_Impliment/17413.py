# https://www.acmicpc.net/problem/17413

import sys
import re 

s_list = re.split(r"(<[^<>]*>| +)", sys.stdin.readline().rstrip())
print(''.join([x[::-1] if x and x[0].isalnum() else x for x in s_list]))