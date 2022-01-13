# n = int(input())
# array = list(map(int, input().split()))

# 이해 안됨

n = 7
array = [15, 11, 4, 8, 5, 2, 4]

array.reverse()
print(array)

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        print(i, j)
        if array[j] < array[i]:
            print(dp[i], dp[j], "dpi, dpj")
            dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        print()


print(n - max(dp))