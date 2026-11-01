n = int(input())
x_list = list(map(int, input().split()))
answer = [None] * n

answer[0] = answer[n - 1] = str((abs(x_list[0] - x_list[-1]) - 1) // 2 + 1)

for k in range(1, n - 1):
    tls = (x_list[k] - x_list[k - 1] - 1) // 2 + 1
    tle = (x_list[k - 1] - x_list[0] - 1) // 2 + 1
    trs = (x_list[k + 1] - x_list[k] - 1) // 2 + 1
    tre = (x_list[-1] - x_list[k + 1] - 1) // 2 + 1
    answer[k] = str(
        min(max(tls + tle, tls + trs + tre), max(trs + tre, trs + tls + tle))
    )

print("\n".join(answer))
