n, q = map(int, input().split())
s_count = [0] * n

q_dict = dict()
for _ in range(q):
    l, r, x = map(int, input().split())
    q_dict.setdefault(x, []).append((l, r))

for key in q_dict.keys():
    range_list = sorted(q_dict[key])
    merged_range_list = []
    for l, r in range_list:
        if not merged_range_list or merged_range_list[-1][1] < l - 1:
            merged_range_list.append([l, r])
        else:
            merged_range_list[-1][1] = max(merged_range_list[-1][1], r)
    q_dict[key] = merged_range_list

delta_list = [0] * (n + 1)

for key in q_dict.keys():
    for l, r in q_dict[key]:
        delta_list[l - 1] += 1
        delta_list[r] -= 1

cur_count = 0
answer = list()
for i in range(n):
    cur_count += delta_list[i]
    answer.append(str(cur_count))
print(" ".join(answer))
