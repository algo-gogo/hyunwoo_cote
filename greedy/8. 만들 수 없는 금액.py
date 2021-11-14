''' 입력 예시
5
3 2 1 1 9
=> 8
'''

from itertools import combinations

n = int(input())
data = list(map(int, input().split()))

sum_lst, combi = [], []
for i in range(1, len(data) + 1):
    temp = list(combinations(data,i))
    combi += temp
# print(combi)
for i in combi:
    sum_lst.append(sum(i))
# print(sum_lst)

for i in range(1, sum(data)):
    if i not in sum_lst:
        print(i)
        break