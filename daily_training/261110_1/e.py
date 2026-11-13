import sys

sys.setrecursionlimit(10**6)

h, w = map(int, input().split())
s_list = [list(input()) for _ in range(h)]


def dfs(x: int, y: int):
    d_list = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]

    for dx, dy in d_list:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and s_list[nx][ny] == "#":
            s_list[nx][ny] = "."
            dfs(nx, ny)


count = 0

for i in range(h):
    for j in range(w):
        if s_list[i][j] == "#":
            dfs(i, j)
            count += 1

print(count)
