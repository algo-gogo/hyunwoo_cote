N = int(input())

answer_lst = []
for _ in range(N):
    temp = input().split()
    answer_lst.append((temp[0], int(temp[1]), int(temp[2]), int(temp[3])))

answer_lst.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in answer_lst:
    print(i[0])