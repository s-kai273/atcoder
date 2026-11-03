n = int(input())
a_list = list(map(int, input().split()))

dp = [""] * n

for i in range(n - 1, -1, -1):
    if a_list[i] == i + 1:
        dp[i] = str(i + 1)
    else:
        dp[i] = dp[a_list[i] - 1]

print(" ".join(dp))
