''' 입력 예시
0001100 => 1
'''

num = input()

answer = 1
temp = num[0]
for i in range(1, len(num)):
    if num[i] == temp:
        continue
    else:
        temp = num[i]
        answer += 1
if answer >= 3:
    answer -= 2
elif answer >= 1:
    answer -= 1

print(answer)


# nList = list(map(int, input()))

# print(nList)

# first = nList[0]
# result = 1
# for i in nList:
#     if first != i:
#         result += 1
#         first = i

# print(result // 2)