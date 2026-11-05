n, m = map(int, input().split())
a_list = list()


def dfs(arr: list[int]):
    if len(arr) == n:
        a_list.append(arr[:])
        return

    start = 1 if len(arr) == 0 else arr[-1] + 10

    for i in range(start, m + 1):
        arr.append(i)
        dfs(arr)
        arr.pop()


dfs([])

for a in a_list:
    print(*a)
