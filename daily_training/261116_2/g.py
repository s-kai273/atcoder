t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    basis = 0
    for ch in s:
        if ch == "1":
            basis += 1

    d_sum = [0]
    for ch in s:
        d = 1 if ch == "1" else -1
        d_sum.append(d_sum[-1] + d)

    min_cost = basis
    min_d_sum = d_sum[0]
    for i in range(1, n + 1):
        cur_d_sum = d_sum[i]
        min_cost = min(min_cost, basis - (cur_d_sum - min_d_sum))
        min_d_sum = min(min_d_sum, cur_d_sum)

    print(min_cost)
