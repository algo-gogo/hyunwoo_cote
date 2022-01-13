# n = int(input())
# input_lst = []
# for i in range(n):
#     input_lst.append(list(map(int, input().split())))

n = 5
input_lst = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]

answer_lst = []
for i in range(n):
    if i == 0:
        answer_lst.append(input_lst[0])
    else:
        answer_lst.append([0] * (i+1))

for i in range(n):
    if i == 0:
        continue
    for j in range(i+1):
        if i == j:
            answer_lst[i][j] = input_lst[i][j] + answer_lst[i - 1][j - 1]
        elif j == 0:
            answer_lst[i][j] = input_lst[i][j] + answer_lst[i - 1][j]
        elif (j + 1) == i:
            answer_lst[i][j] = input_lst[i][j] + max(answer_lst[i - 1][j - 1], answer_lst[i - 1][j])
        else:
            answer_lst[i][j] = input_lst[i][j] + max(answer_lst[i - 1][j - 1], answer_lst[i - 1][j])

# print(answer_lst)
answer_lst = sum(answer_lst, [])
print(max(answer_lst))


