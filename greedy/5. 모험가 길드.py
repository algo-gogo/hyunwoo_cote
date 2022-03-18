''' 입력 예시
5
2 3 1 2 2  
=> 2
'''

n = int(input())
data = list(map(int, input().split()))

data.sort()

cnt = 0
while(len(data)):
    cnt += 1
    temp = data[-1]
    for _ in range(temp):
        data.pop(-1)

print(cnt)