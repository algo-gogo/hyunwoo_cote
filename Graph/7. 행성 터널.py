### 메모리 초과

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트가 아니면 루트 찾을 때까지 재귀로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) ## 메모이제이션 기능!!!
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v = int(input())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
answer = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

point_lst = []
for _ in range(v):
    point_lst.append(list(map(int, input().split())))

for i_ind, i_val in enumerate(point_lst):
    for j_ind, j_val in enumerate(point_lst):
        if i_ind == j_ind:
            continue
        else:
            edges.append((
                min(abs(i_val[0] - j_val[0]), abs(i_val[1] - j_val[1]), abs(i_val[2] - j_val[2])),
                i_ind + 1, j_ind + 1))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost

print(answer)