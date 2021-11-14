''' 입력 예시
5 8 3
2 4 5 4 6
=> 46
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data = sorted(data)
biggest, sec_biggest = data[-1], data[-2]

answer = 0
while(m > 0):
    if m > k:
        answer += biggest * k
        m -= k
    else:
        answer += sec_biggest
        m -= 1

print(answer)

'''Tip
반복되는 수열을 파악하자
예시) 6,6,6,5
int(M/(K+1)) * K + M % (K+1)
'''
