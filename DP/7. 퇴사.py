# gif 나온 사이트: https://jrc-park.tistory.com/119

n = int(input())
t, p = [], []
dp = [0] * (n + 1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n - 1, -1, -1):
    print(i)
    time = t[i] + 1
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
    print(dp[i])

print(max_value)