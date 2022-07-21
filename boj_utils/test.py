from itertools import combinations
import sys

sys.stdin = open('/home/jsg/git/nikoneko/boj_utils/input.txt', 'r')

N = int(input())
cost = list()
for n in range(N):
    cost_row = list(map(int, input().split()))
    cost.append(cost_row)

value = 600

for x1 in range(1, len(cost)-1):
    for y1 in range(1, len(cost[0])-1):
        first_pos = [x1, y1]

        for x2 in range(1, len(cost)-1):
            for y2 in range(1, len(cost[0])-1):
                second_pos_temp = [x2, y2]
                diff12 = abs(first_pos[0]-second_pos_temp[0])+abs(first_pos[1]-second_pos_temp[1])
                if diff12 >= 3:
                    second_pos = second_pos_temp

                    for x3 in range(1, len(cost)-1):
                        for y3 in range(1, len(cost[0])-1):
                            third_pos_temp = [x3, y3]
                            diff13 = abs(first_pos[0]-third_pos_temp[0])+abs(first_pos[1]-third_pos_temp[1])
                            diff23 = abs(second_pos[0]-third_pos_temp[0])+abs(second_pos[1]-third_pos_temp[1])
                            if diff13 >= 3 and diff23 >= 3:
                                third_pos = third_pos_temp
                                value1 = cost[first_pos[1]][first_pos[0]] + cost[first_pos[1]][first_pos[0]-1] + cost[first_pos[1]-1][first_pos[0]] + cost[first_pos[1]+1][first_pos[0]] + cost[first_pos[1]][first_pos[0]+1]
                                value2 = cost[second_pos[1]][second_pos[0]] + cost[second_pos[1]][second_pos[0]-1] + cost[second_pos[1]-1][second_pos[0]] + cost[second_pos[1]+1][second_pos[0]] + cost[second_pos[1]][second_pos[0]+1]
                                value3 = cost[third_pos[1]][third_pos[0]] + cost[third_pos[1]][third_pos[0]-1] + cost[third_pos[1]-1][third_pos[0]] + cost[third_pos[1]+1][third_pos[0]] + cost[third_pos[1]][third_pos[0]+1]
                                value = min(value, value1+value2+value3)
                                # print("first: {},\tsecond: {},\tthird: {}".format(first_pos, second_pos, third_pos))
                                # print("first: {},\tsecond: {},\tthird: {}".format(value1, value2, value3))
                                # print(first_pos-second_pos)
                    

print(value)