''' 입력 예시
25 5 => 2
'''

n, k = map(int, input().split())

cnt = 0
# while(n != 1):
#     if n % k == 0:
#         n /= k
#     else:
#         n -= 1
#     cnt += 1

# print(cnt)

""" Tip n이 엄청나게 큰숫자 (100만) 이면 1씩 빼는게 효율적이지 않다
while(n != 1):
    if n % k == 0:
        n /= k
        cnt += 1
    else:
        cnt += n % k
        n -= n % k
print(cnt)
"""