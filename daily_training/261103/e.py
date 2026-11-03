n = int(input())
a_list = list(map(int, input().split()))

dp = [-1] * n

for i in range(n - 1, -1, -1):
    if a_list[i] == i + 1:
        dp[i] = i + 1
    else:
        dp[i] = dp[a_list[i] - 1]

print(*dp)
