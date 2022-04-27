''' 입력 예시
3
10
20
40

=> 100
'''
import heapq

N = int(input())

num_lst = []
for _ in range(N):
    heapq.heappush(num_lst, int(input()))

answer = 0

while num_lst:
    if len(num_lst) == 1:
        break
    a = heapq.heappop(num_lst)
    b = heapq.heappop(num_lst)
    temp = a + b
    answer += temp
    heapq.heappush(num_lst, temp)

print(answer)