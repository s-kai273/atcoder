n = int(input())
s_list = list()
max_len = 0
for _ in range(n):
    s = list(input())
    s_list.append(s)
    max_len = max(max_len, len(s))

for i in range(max_len):
    t = list()
    for j in range(n - 1, -1, -1):
        if i > len(s_list[j]) - 1:
            t.append("*")
        else:
            t.append(s_list[j][i])
    print("".join(t).rstrip("*"))
