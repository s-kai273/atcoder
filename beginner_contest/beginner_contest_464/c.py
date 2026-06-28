n, m = map(int, input().split())
total_color_count = 0
color_counter = dict()
change_dict = dict()
for _ in range(n):
    a, d, b = map(int, input().split())
    if a not in color_counter:
        total_color_count += 1
    change_dict.setdefault(d, []).append((a, b))
    color_counter[a] = color_counter.get(a, 0) + 1
for j in range(1, m + 1):
    if j in change_dict:
        for a, b in change_dict[j]:
            color_counter[a] -= 1
            if color_counter[a] == 0:
                total_color_count -= 1
            color_counter[b] = color_counter.get(b, 0) + 1
            if color_counter[b] == 1:
                total_color_count += 1
    print(total_color_count)
