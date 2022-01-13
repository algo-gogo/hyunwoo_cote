test_case = int(input())

n_lst, m_lst = [], []
whole_input_lst = []

for i in range(test_case):
    n, m = tuple(map(int, input().split()))
    n_lst.append(n)
    m_lst.append(m)
    input_lst = list(map(int, input().split()))
    whole_input_lst.append(input_lst)

# n, m = 3, 4
# input_lst = [1,3,3,2,2,1,4,1,0,6,4,7]

# n, m = 4, 4
# input_lst = [1,3,1,5,2,2,4,1,5,0,2,3,0,6,1,2]

def solution(n, m, input_lst):

    out_lst, in_lst = [], []

    for ind, val in enumerate(input_lst):
        if ind == 0:
            in_lst.append(val)
        elif ind == (n * m - 1):
            in_lst.append(val)
            out_lst.append(in_lst)
        elif ind % m == 0:
            out_lst.append(in_lst)
            in_lst = []
            in_lst.append(val)
        elif ind % m != 0:
            in_lst.append(val)
        
    answer_lst = []
    for i in range(n):
        answer_lst.append([0] * m)

    for ind, val in enumerate(answer_lst):
        val[0] = out_lst[ind][0]

    # print(answer_lst)

    for j in range(m):
        if j == 0:
            continue
        for i in range(n):
            # print(i,j)
            if (i - 1) == -1: # 맨 위에 있을떄
                answer_lst[i][j] = out_lst[i][j] + max(answer_lst[i][j - 1], answer_lst[i + 1][j - 1])
            elif (i + 1) == n: # 맨 아래에 있을떄
                answer_lst[i][j] = out_lst[i][j] + max(answer_lst[i][j - 1], answer_lst[i - 1][j - 1])
            else: # 중간에 있을떄
                answer_lst[i][j] = out_lst[i][j] + max(answer_lst[i][j - 1], answer_lst[i - 1][j - 1], answer_lst[i + 1][j - 1])

    answer_lst = sum(answer_lst, [])
    print(max(answer_lst))


for i in range(test_case):
    solution(n_lst[i], m_lst[i], whole_input_lst[i])
