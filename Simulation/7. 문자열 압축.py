''' 입력 예시
aabbaccc => 7
ababcdcdababcdcd => 9
abcabcdede => 8
abcabcabcabcdededededede => 14
xababcdcdababcdcd => 17
'''

s = "xababcdcdababcdcd"
string_length = len(s)

whole_lst = []
temp_lst = []
for i in range(1, string_length):
    temp_lst = []
    for j in range(0, string_length,i):
        temp_lst.append(s[j : j + i])
    whole_lst.append(temp_lst)

answer = []
cnt = 0

min_num = 1000
for j in whole_lst:
    final_lst = [j[0]]
    cnt = 1
    j.append(1)
    for i in range(len(j) - 1):
        if j[i] == j[i+1]:
            cnt += 1
        else:
            final_lst.append(cnt)
            final_lst.append(j[i+1])
            cnt = 1

    temptemp = []
    for i in final_lst:
        if i != 1:
            temptemp.append(i)
    temptemp = list(map(str,temptemp))
    if min_num > len("".join(temptemp)):
        min_num = len("".join(temptemp))

if string_length == 1:
    print(1)
else:
    print(min_num)
