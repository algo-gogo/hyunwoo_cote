''' 입력 예시
aabbaccc => 7
ababcdcdababcdcd => 9
abcabcdede => 8
abcabcabcabcdededededede => 14
xababcdcdababcdcd => 17
'''
from typing import final


s = "aabbaccc"
string_length = len(s)
whole_lst = []
temp_lst = []
for i in range(1, string_length // 2):
    temp_lst = []
    for j in range(0,string_length,i):
        # if len(s[j:j+i]) == i:
        temp_lst.append(s[j:j+i])
    whole_lst.append(temp_lst)

answer = []
cnt = 0
print(whole_lst)


for j in whole_lst:
    final_lst = [j[0]]
    cnt = 1
    j.append(2.2)
    for i in range(len(j) - 1):
        print(j[i], j[i+1])
        if j[i] == j[i+1]:
            # final_lst.append(j[i])
            cnt += 1
        else:
            final_lst.append(cnt)
            final_lst.append(j[i+1])
            cnt = 1

    temptemp = []
    for i in final_lst:
        if i != 1 or i != 2.2:
            temptemp.append(i)

    print(temptemp)
