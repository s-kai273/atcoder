h, w, x, y = map(int, input().split())
s_list = [list(input()) for _ in range(h)]
t = input()

visited = set()

x -= 1
y -= 1

d_dict = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

for ch in t:
    dx, dy = d_dict[ch]
    nx, ny = x + dx, y + dy
    if s_list[nx][ny] == "#":
        continue

    if s_list[nx][ny] == "@" and (nx, ny) not in visited:
        visited.add((nx, ny))

    x = nx
    y = ny

print(f"{x + 1} {y + 1} {len(visited)}")
