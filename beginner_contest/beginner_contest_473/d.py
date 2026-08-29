n, k = map(int, input().split())
answer = list()


def dfs(i: int, a_parts: list[str], cur_sum: int):
    if i > n or cur_sum > k:
        return
    for a in range(k + 1):
        a_parts.append(str(a))
        cur_sum += i * a
        if cur_sum == k:
            if i == n:
                answer.append(a_parts.copy())
            else:
                answer.append(a_parts.copy() + ["0"] * (n - i))
        elif i < n and cur_sum < k:
            dfs(i + 1, a_parts, cur_sum)
        a_parts.pop()
        cur_sum -= i * a
        if cur_sum + i * a >= k:
            break


dfs(1, [], 0)
for comb in answer:
    print(" ".join(comb))
