''' 입력 예시
5 3
1 3 2 3 2
=> 8

8 5
1 5 4 3 2 4 5 2
=> 25
'''

from itertools import combinations

n, k = map(int, input().split())
data = list(map(int, input().split()))

combi = list(combinations(data,2))
answer = []
for i in combi:
    if i[0] != i[1]:
        answer.append(i)

print(len(answer))
