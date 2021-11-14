''' 입력 예시
5 3
1 3 2 3 2
=> 8

8 5
1 5 4 3 2 4 5 2
=> 25
'''

import copy

def solution(food_times, k):
    if k >= sum(food_times):
        return -1
    elif k == sum(food_times) - 1:
        return food_times.index(max(food_times)) + 1
    
    ori_food_times = copy.deepcopy(food_times)
    left_cnt = 0
    cnt = 0
    temp = food_times[0]
    while left_cnt != k:
        if food_times[left_cnt % len(food_times)] == 0:
            left_cnt += 1
            continue
        food_times[left_cnt % len(food_times)] -= 1
        left_cnt += 1
        cnt += 1
        
    return ori_food_times[cnt % len(food_times)] + 1