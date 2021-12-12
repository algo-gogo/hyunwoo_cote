N = int(input())

num_lst = []
for _ in range(N):
    num_lst.append(int(input()))


answer = 0

while num_lst:
    num_lst.sort()

    if len(num_lst) == 1:
        break
    a = num_lst.pop(0)
    b = num_lst.pop(0)
    temp = a + b
    answer += temp
    num_lst.insert(0, temp)

print(answer)