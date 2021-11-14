''' 입력 예시
02984 => 576
567 => 210
'''

num = input()

answer = 1
for i in num:
    if int(i) == 0:
        answer += int(i)
    elif int(i) == 1:
        answer += int(i)
    else:
        answer *= int(i)
print(answer)
