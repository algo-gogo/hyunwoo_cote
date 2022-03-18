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

cycle_bool = False # 사이클 발생 여부

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    # 사이클 발생 경우
    if find_parent(parent, a) == find_parent(parent, b):
        cycle_bool = True
        break
    # 사이클 발생 안하면 union 실행
    else:
        union_parent(parent, a, b)

if cycle_bool:
    print("사이클 발생")
else:
    print("사이클 노발생")