from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
# n, m = 4, 4

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
# graph.append([0, 0, 1, 1])
# graph.append([0, 0, 1, 0])
# graph.append([1, 1, 0, 0])
# graph.append([0, 2, 0, 1])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

zero_place = []
for i, i_val in enumerate(graph):
    for j, j_val in enumerate(i_val):
        if j_val == 0:
            zero_place.append([i, j])

zero_combi = list(combinations(zero_place, 3))


def bfs(x, y, graph):
    queue = deque()
    queue.append((x, y))
    while queue:
        # print(queue)
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 2:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))


def findSafe(graph):
    cnt = 0
    for i in graph:
        for j in i:
            if j == 0:
                cnt += 1

    # print(cnt)
    # for i in graph:
    #     print(i)
    # print()
    return cnt


answer_lst = []

for i in zero_combi:
    temp_graph = copy.deepcopy(graph)
    temp_graph[i[0][0]][i[0][1]] = 1
    temp_graph[i[1][0]][i[1][1]] = 1
    temp_graph[i[2][0]][i[2][1]] = 1

    # print(temp_graph)

    a, b = -1, -1
    for i, i_val in enumerate(temp_graph):
        for j, j_val in enumerate(i_val):
            if j_val == 2:
                a, b = i, j
                bfs(a, b, temp_graph)

    answer_lst.append(findSafe(temp_graph))
    continue


print(max(answer_lst))