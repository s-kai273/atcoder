import sys

sys.setrecursionlimit(10**8)
n = int(input())
x_sum_dict = dict()


def dfs(num: int) -> int:
    if num < 2:
        return 0
    if num in x_sum_dict:
        return x_sum_dict[num]
    result = dfs(num // 2) + dfs((num + 1) // 2) + num
    x_sum_dict[num] = result
    return result


print(dfs(n))
