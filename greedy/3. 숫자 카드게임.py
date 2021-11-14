''' 입력 예시
3 3
3 1 2
4 1 4
2 2 2
=> 2

2 4
7 3 1 8
3 3 3 4
=> 3
'''

m, n = map(int, input().split())
data = []
for _ in range(m):
    data.append(list(map(int, input().split())))

temp = []
for i in data:
    temp.append(min(i))

print(max(temp))