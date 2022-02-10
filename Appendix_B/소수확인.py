# 한 숫자가 소수인지 판별하는 함수
# O(x*1/2)
import math
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# 에라토스테네스의 체
# N 보다 작거나 같은 모든 소수를 찾을떄 사용
# O(NloglogN)
import math

n = 1000
array = [True for i in range(n + 1)] # 초기엔 모든 수가 소수(True)인걸로 초기화
array[1] = 0 # 1은 소수가 아님

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 ㅑ의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
            
for i in range(2, n + 1):
    if array[i]:
        print(i, end= " ")