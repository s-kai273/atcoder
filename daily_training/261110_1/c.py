n = int(input())
s_list = list()
for _ in range(n):
    s_list.append(list(input()))

win_dict = dict()

for i in range(n):
    for j in range(n):
        win_dict.setdefault(i + 1, 0)
        if s_list[i][j] == "o":
            win_dict[i + 1] += 1

players = sorted(win_dict.keys(), key=lambda i: -win_dict[i])

print(*players)
