import math

m, n = map(int, input().split())

array = [True for i in range(n + 1)] # 초기엔 모든 수가 소수(True)인걸로 초기화
if len(array) >= 2:
    array[1] = 0 # 1은 소수가 아님

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 ㅑ의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
       
for i in range(m, n + 1):
    if array[i]:
        print(i)