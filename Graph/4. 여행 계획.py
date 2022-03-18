## 개선된 서로소 집합 알고리즘

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
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(1, v + 1):
    path_lst = list(map(int, input().split()))
    for idx, path in enumerate(path_lst):
        if path == 1:
            union_parent(parent, i, path + 1)

travel_lst = list(map(int, input().split()))
answer_lst = []
for travel in travel_lst:
    answer_lst.append(find_parent(parent, travel))

if min(answer_lst) == max(answer_lst):
    print("YES")