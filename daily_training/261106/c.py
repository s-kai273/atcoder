h, w, x, y = map(int, input().split())
s_list = list()

for _ in range(h):
    s_list.append(list(input()))

t = input()

house_count = 0
visited = set()

x -= 1
y -= 1
visited.add((x, y))

d_dict = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

for ch in t:
    dx, dy = d_dict[ch]
    if s_list[x + dx][y + dy] != "#":
        if (x + dx, y + dy) not in visited:
            visited.add((x + dx, y + dy))
            house_count += 1 if s_list[x + dx][y + dy] == "@" else 0
        x += dx
        y += dy

print(f"{x + 1} {y + 1} {house_count}")
