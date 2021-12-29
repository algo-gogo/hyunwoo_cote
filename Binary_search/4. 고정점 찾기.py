# 시간복잡도 O(logN)
def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        target = mid
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

import sys
N = int(input())
input_data = list(map(int,sys.stdin.readline().rstrip().split()))

answer = binary_search(input_data, 0, N-1)

if answer == None:
    print(-1)
else:
    print(answer)