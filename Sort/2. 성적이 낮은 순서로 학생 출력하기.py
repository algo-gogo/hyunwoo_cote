''' 입력 예시
2
홍길동 95
이순신 77

=> 이순신 홍길동
'''

N = int(input())

answer_lst = []
for _ in range(N):
    temp = input().split()
    answer_lst.append((temp[0], int(temp[1])))

answer_lst.sort(key=lambda x:x[1])

for i in answer_lst:
    print(i[0], end=" ")