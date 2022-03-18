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

n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

answer_lst = []

for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            answer_lst.append("YES")
        else:
            answer_lst.append("NO")

for i in answer_lst:
    print(i)