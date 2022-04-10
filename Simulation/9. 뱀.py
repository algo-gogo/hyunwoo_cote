''' 입력 예시
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
'''


# board_num = int(input())
# apple_num = int(input())
# map_lst = [[0] * (board_num + 1) for _ in range(board_num + 1)]
# direction_info = []

# for _ in range(apple_num):
#     x, y = map(int, input().split())
#     map_lst[x][y] = 1

# direction_num = int(input())
# for _ in range(direction_num):
#     x, c = input().split()
#     direction_info.append((int(x), c))

# # 동 남 서 북 순서
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def turn(direction, c):
#     if c == "L": # 왼쪽으로 90도 회전
#         direction = (direction - 1) % 4
#     else: # 오른쪽으로 90도 회전
#         direction = (direction + 1) % 4
#     return direction

# def simulate():
#     snake_x, snake_y = 1, 1
#     map_lst[snake_x][snake_y] = 2
#     direction, time, next_turn = 0, 0, 0
#     snake_lst = [(snake_x, snake_y)]

#     while True:
#         next_x = snake_x + dx[direction]
#         next_y = snake_y + dy[direction]

#         # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치이면
#         if 1 <= next_x and next_x <= board_num and 1 <= next_y and next_y <= board_num and map_lst[next_x][next_y] != 2:
#             # 사과 없으면
#             if map_lst[next_x][next_y] == 0:
#                 map_lst[next_x][next_y] = 2
#                 snake_lst.append((next_x, next_y))
#                 temp_x, temp_y = snake_lst.pop(0)
#                 map_lst[temp_x][temp_y] = 0
#             # 사과 있으면
#             if map_lst[next_x][next_y] == 1:
#                 map_lst[next_x][next_y] = 2
#                 snake_lst.append((next_x, next_y))
#         else:
#             time += 1
#             break
#         snake_x, snake_y = next_x, next_y
#         time += 1
#         if next_turn < 1 and time == direction_info[next_turn][0]: #회전 타임
#             direction = turn(direction, direction_info[next_turn][1])
#             next_turn += 1

#     return time

# print(simulate())
n = int(input())
k = int(input())
map_lst = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    map_lst[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    map_lst[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    next_turn_info = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and map_lst[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if map_lst[nx][ny] == 0:
                map_lst[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                map_lst[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if map_lst[nx][ny] == 1:
                map_lst[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        if next_turn_info < l and time == info[next_turn_info][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[next_turn_info][1])
            next_turn_info += 1
    return time

print(simulate())
