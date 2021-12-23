N,K = map(int, input().split())

graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
graph.append([1,0,2])
graph.append([0,0,0])
graph.append([3,0,0])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus_dict = {}
for i, i_val in enumerate(graph):
    for j, j_val in enumerate(i_val):
        for number in range(1, K+1):
            if j_val == number:
                virus_dict[number] = [(i,j)]

print(virus_dict)
import copy
while True:
    temp_dict = copy.deepcopy(virus_dict)
    for number in range(1, K+1):
        print(2)
        for i,j in virus_dict[number]:
            print(i,j)
            for temp in range(4):
                nx = i + dx[temp]
                ny = j + dy[temp]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue 
                if graph[nx][ny] == 0:
                    graph[nx][ny] == number
                    virus_dict[number].append((nx, ny))

    print(3)
    if virus_dict == temp_dict:
        break

print(virus_dict)

# def bfs(x, y, graph):
#     queue = deque()
#     queue.append((x, y))
#     while queue:
#         print(queue)
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if graph[nx][ny