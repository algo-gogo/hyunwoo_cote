''' 입력 예시
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
=> 6
'''

# n, m = map(int, input().split())
# character = list(map(int, input().split()))
game_map = []
# for _ in range(m):
#     game_map.append(list(input().split()))

# 예시
n, m = 4, 4
x, y, direction = (1, 1, 0)
game_map.append([1, 1, 1, 1])
game_map.append([1, 0, 0, 1])
game_map.append([1, 1, 0, 1])
game_map.append([1, 1, 1, 1])

visited = [[0] * m for _ in range(n)]
visited[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction

cnt = 1
turn_cnt = 0

while True:
    direction = turn_left(direction)
    next_x = x + dx[direction]
    next_y = y + dy[direction]

    if visited[next_x][next_y] == 0 and game_map[next_x][next_y] == 0:  ## 방문 안했거나 육지 일때
        visited[next_x][next_y] = 1
        x, y = next_x, next_y
        cnt += 1
        turn_cnt = 0
        continue
    else:
        turn_cnt += 1
    
    if turn_cnt == 4: #4방향 다 확인한 경우
        next_x = x - dx[direction]
        next_x = x - dx[direction]
        if game_map[next_x][next_y] == 0:
            x, y = next_x, next_y
        else:
            break
        turn_cnt = 0
    

print(cnt)