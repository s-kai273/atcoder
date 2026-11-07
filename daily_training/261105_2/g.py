n, m = map(int, input().split())
a_list = list()


def dfs(arr: list[int]):
    if len(arr) == n:
        a_list.append(arr[:])
        return

    start = 1 if len(arr) == 0 else arr[-1] + 10
    r = n - len(arr) - 1
    end = m - 10 * r

    for i in range(start, end + 1):
        arr.append(i)
        dfs(arr)
        arr.pop()


dfs([])

print(len(a_list))
for a in a_list:
    print(*a)
