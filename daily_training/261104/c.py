n = int(input())
s_list = list()
max_len = 0
for _ in range(n):
    s = list(input())
    s_list.append(s)
    max_len = max(max_len, len(s))

t_list = list()
for i in range(max_len):
    t = list()
    empty_starts_at = -1
    for j in range(n - 1, -1, -1):
        if i > len(s_list[j]) - 1:
            if empty_starts_at == -1:
                empty_starts_at = j
        else:
            if empty_starts_at != -1:
                t.extend(["*"] * (empty_starts_at - j))
                empty_starts_at = -1
            t.append(s_list[j][i])
    t_list.append(t)

for t in t_list:
    print("".join(t))
