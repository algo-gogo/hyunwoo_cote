"""
n	edges	                    result
5	[[0,1],[0,2],[1,3],[1,4]]	16
4	[[2,3],[0,1],[1,2]]	        8
"""

from itertools import permutations

def bfs(start, end, n, graph):
    root = [start]
    way = [0]*(n+1)
    while root:
        k = root.pop(0)
        if k == end:
            break
        for i in graph[k]:
            root.append(i[0])
            way[i[0]] = way[k] + i[1]
    return way[end]
    
def solution(n, edges):
    answer = 0
    arr = range(n)
    graph = [[] for _ in range(n+1)]
    for edge in edges:
        x,y = edge
        graph[x].append([y, 1])
        graph[y].append([x, 1])
    arr_per_lst = list(permutations(arr, 3))

    for arr_per in arr_per_lst:
        temp1 = bfs(arr_per[0],arr_per[1], n, graph)
        temp2 = bfs(arr_per[1],arr_per[2], n, graph)
        temp3 = bfs(arr_per[0],arr_per[2], n, graph)
        if temp1 + temp2 == temp3:
            answer += 1
    return answer

n_1 = 5
edges_1 = [[0,1],[0,2],[1,3],[1,4]]

n_2 = 4
edges_2 = [[2,3],[0,1],[1,2]]

print(solution(n_1, edges_1))
print(solution(n_2, edges_2))