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

for ch in t:
    if ch == "U" and s_list[x - 1][y] != "#":
        if (x - 1, y) not in visited:
            visited.add((x - 1, y))
            house_count += 1 if s_list[x - 1][y] == "@" else 0
        x -= 1
    elif ch == "D" and s_list[x + 1][y] != "#":
        if (x + 1, y) not in visited:
            visited.add((x + 1, y))
            house_count += 1 if s_list[x + 1][y] == "@" else 0
        x += 1
    elif ch == "L" and s_list[x][y - 1] != "#":
        if (x, y - 1) not in visited:
            visited.add((x, y - 1))
            house_count += 1 if s_list[x][y - 1] == "@" else 0
        y -= 1
    elif ch == "R" and s_list[x][y + 1] != "#":
        if (x, y + 1) not in visited:
            visited.add((x, y + 1))
            house_count += 1 if s_list[x][y + 1] == "@" else 0
        y += 1

print(f"{x + 1} {y + 1} {house_count}")
