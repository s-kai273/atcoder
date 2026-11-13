from collections import deque

h, w = map(int, input().split())
s_list = list()

for _ in range(h):
    s_list.append(list(input()))

si, sj = None, None
gi, gj = None, None

for i in range(h):
    for j in range(w):
        if s_list[i][j] == "S":
            si, sj = i, j
        if s_list[i][j] == "G":
            gi, gj = i, j

queue = deque([([], si, sj, 0, 0)])
visited = set()
count = None

while queue and len(visited) < h * w:
    cmd_list, i, j, pdi, pdj = queue.popleft()
    visited.add((i, j))

    for cmd, di, dj in [
        ("R", 0, 1),
        ("L", 0, -1),
        ("D", 1, 0),
        ("U", -1, 0),
    ]:
        ni, nj = i + di, j + dj
        if not (0 <= ni < h) or not (0 <= nj < w) or (ni, nj) in visited:
            continue

        s = s_list[ni][nj]
        if (
            s == "#"
            or (s == "o" and di != pdi and dj != pdj)
            or (s == "x" and di == pdi and dj == pdj)
        ):
            continue

        if s == "G":
            break
        queue.append((cmd_list + [cmd], ni, nj, di, dj))


if count:
    print("Yes")
    print(count)
else:
    print("No")
