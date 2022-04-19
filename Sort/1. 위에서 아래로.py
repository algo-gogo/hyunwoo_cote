''' 입력 예시
3
15
27
12

=> 27 15 12
'''

N = int(input())

answer_lst = []
for _ in range(N):
    answer_lst.append(int(input()))

answer_lst.sort(reverse=True)

for i in answer_lst:
    print(i, end=" ")