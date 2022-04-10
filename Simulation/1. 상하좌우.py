''' 입력 예시
5 
R R R U D D
=> 3 4
'''

# n = int(input())
# data = list(input().split())
n = 5
data = ['R', 'R', 'R', 'U', 'D', 'D']

start = [1, 1]
for i in range(len(data)):
    if data[i] == "L":
        start[1] -= 1
        if start[1] == 0:
            start[1] += 1
    elif data[i] == "R":
        start[1] += 1
        if start[1] == n + 1:
            start[1] -= 1
    elif data[i] == "U":
        start[0] -= 1
        if start[0] == 0:
            start[0] += 1
    elif data[i] == "D":
        start[0] += 1
        if start[0] == n + 1:
            start[0] -= 1
    
print(start)