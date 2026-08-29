n, k = map(int, input().split())
answer = list()


def dfs(i: int, a_parts: list[int], cur_sum: int):
    if i == n:
        remain = k - cur_sum
        if remain % n == 0:
            answer.append(a_parts.copy() + [remain // n])
        return

    for a in range(k + 1):
        a_parts.append(a)
        cur_sum += i * a
        if cur_sum == k:
            answer.append(a_parts.copy() + [0] * (n - i))
        elif i < n and cur_sum < k:
            dfs(i + 1, a_parts, cur_sum)
        a_parts.pop()
        cur_sum -= i * a
        if cur_sum + i * a >= k:
            break


dfs(1, [], 0)
for comb in answer:
    comb = [str(val) for val in comb]
    print(" ".join(comb))
