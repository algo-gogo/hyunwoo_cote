def solution(goods):
    goods_lst = [[] for _ in range(len(goods))]
    goods_dic = {}

    for idx, good in enumerate(goods):
        for i in range(len(good)):
            for j in range(len(good) - i):
                goods_lst[idx].append(good[j : j + i + 1])

    set_lst = []
    for i in goods_lst:
        result = []
        for val in i:
            if val not in result:
                result.append(val)
        set_lst.append(result)


    # print(set_lst)

    for i in set_lst:
        for j in i:
            if j in goods_dic:
                goods_dic[j] += 1
            else:
                goods_dic[j] = 1

    # print()
    # print(goods_dic)

    goods_lst_final = [[] for _ in range(len(goods))]
    for i, val in enumerate(goods_lst):
        for j in val:
            if goods_dic[j] == 1:
                goods_lst_final[i].append(j)

    # print()
    # print(goods_lst_final)
    for i in goods_lst_final:
        if len(i) == 0:
            i.extend("*")
    # print(goods_lst_final)

    answer_lst = [[] for _ in range(len(goods))]

    for idx, val in enumerate(goods_lst_final):
        shortest_len = len(val[0])
        for j in val:
            if len(j) == shortest_len:
                answer_lst[idx].append(j)


    final_answer_lst = []

    set_lst = []
    for i in answer_lst:
        result = []
        for val in i:
            if val not in result:
                result.append(val)
        set_lst.append(result)


    for i in set_lst:
        i.sort()
        tmp = " ".join(i)
        final_answer_lst.append(tmp)


    real_final_answer = []

    for i in final_answer_lst:
        if i == "*":
            real_final_answer.append("None")
        else:
            real_final_answer.append(i)

    print(real_final_answer) 

    


goods1 = ["pencil", "cilicon", "contrabase", "picturelist"]
goods2 = ["abcdeabcd", "cdabe", "abce", "bcdeab"]
solution(goods1)
solution(goods2)