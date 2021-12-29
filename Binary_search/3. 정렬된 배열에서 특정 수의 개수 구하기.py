# 시간복잡도 O(N)

# import sys
# N, x = input().split()
# input_data = sys.stdin.readline().rstrip()
# ans = input_data.count(x)
# if ans == 0:
#     print(-1)
# else:
#     print(ans)
    
# 시간복잡도 O(logN)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

import sys
N, x = tuple(map(int, input().split()))
input_data = list(map(int,sys.stdin.readline().rstrip().split()))

from bisect import bisect_left, bisect_right

def count_by_range(array, left_val, right_val):
    right_idx = bisect_right(array, right_val)
    left_idx = bisect_left(array, left_val)
    return right_idx - left_idx

answer = count_by_range(input_data, x, x)

if answer == 0:
    print(-1)
else:
    print(answer)