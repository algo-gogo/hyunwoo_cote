''' 입력 예시
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2 
=> 5
'''

from itertools import combinations

n, m = map(int, input().split())
chicken_map = []
for _ in range(n):
    chicken_map.append(list(input().split()))

# n, m = 5, 2

# chicken_map.append(["0", "2", "0", "1", "0"])
# chicken_map.append(["1", "0", "1", "0", "0"])
# chicken_map.append(["0", "0", "0", "0", "0"])
# chicken_map.append(["2", "0", "0", "1", "1"])
# chicken_map.append(["2", "2", "0", "1", "2"])

chicken_lst, house_lst = [], []
for i_ind, i_val in enumerate(chicken_map):
    for j_ind, j_val in enumerate(i_val):
        if j_val == "2":
            chicken_lst.append([i_ind, j_ind])
        elif j_val == "1":
            house_lst.append([i_ind, j_ind])


# a = [[1, 2], [2, 2], [4, 4]]
# print(chicken_map)
chicken_combi = list(combinations(chicken_lst, m))
# print("qwe", chicken_combi)
answer_lst = []
for i in chicken_combi:
    answer = 0
    for house in house_lst:
        minimum = 100000
        for j in i:
            temp_len = 0
            temp_len += abs(j[0] - house[0])
            temp_len += abs(j[1] - house[1])
            if minimum > temp_len:
                minimum = temp_len
        answer += minimum
    # print(temp_len, "temp_len")
    if temp_len < minimum:
        minimum = temp_len
    answer_lst.append(answer)

# print(answer_lst)
print(min(answer_lst))