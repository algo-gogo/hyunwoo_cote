from collections import deque

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

shark_x, shark_y = 0, 0
# 상어 위치 알아내기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0
            shark_x, shark_y = i, j
            break
shark_size = 2
move_num = 0
eat = 0
while True:
    q = deque()
    q.append((shark_x, shark_y, 0))
    visited = [[False] * n for _ in range(n)]
    flag = 1e9
    fish = []
    while q:
        x, y, count = q.popleft()

        if count > flag:
            break
        for direction in range(4):
            nx, ny = x + dx[direction], y + dy[direction]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if arr[nx][ny] > shark_size or visited[nx][ny]:
                continue

            if arr[nx][ny] != 0 and arr[nx][ny] < shark_size: # 상어가 fish 보다 작거나, 크기가 0이 아닌 fish가 있으면
                fish.append((nx, ny, count + 1))
                flag = count
            visited[nx][ny] = True
            q.append((nx, ny, count + 1))

    if len(fish) > 0:
        fish.sort()
        x, y, move = fish[0][0], fish[0][1], fish[0][2]
        move_num += move
        eat += 1
        arr[x][y] = 0
        if eat == shark_size:
            shark_size += 1
            eat = 0
        shark_x, shark_y = x, y
    else:
        break

print(move_num)