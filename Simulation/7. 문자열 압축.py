''' 입력 예시
aabbaccc => 7
ababcdcdababcdcd => 9
abcabcdede => 8
abcabcabcabcdededededede => 14
xababcdcdababcdcd => 17
'''

s = "ababcdcdababcdcd"
string_length = len(s)
whole_lst = []
temp_lst = []
for i in range(1, string_length):
    temp_lst = []
    for j in range(0,string_length,i):
        # if len(s[j:j+i]) == i:
        temp_lst.append(s[j:j+i])
    whole_lst.append(temp_lst)

answer = []
cnt = 0
# print(whole_lst)

min = 1000
for j in whole_lst:
    final_lst = [j[0]]
    cnt = 1
    j.append(1)
    for i in range(len(j) - 1):
        # print(j[i], j[i+1])
        if j[i] == j[i+1]:
            # final_lst.append(j[i])
            cnt += 1
        else:
            final_lst.append(cnt)
            final_lst.append(j[i+1])
            cnt = 1

    print(final_lst, "poi")
    temptemp = []
    for i in final_lst:
        if i != 1:
            # print(i, "qwe")
            temptemp.append(i)
    temptemp = list(map(str,temptemp))
    # print("sdf", temptemp)
    if min > len("".join(temptemp)):
        min = len("".join(temptemp))

print(min, "qweqwrqweqwe")
