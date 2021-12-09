from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# print(graph)
distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])
while q:
    # print(q)
    # print(distance)
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# print(distance)
check_flag = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check_flag = True

if not check_flag:
    print(-1)