n = int(input())
count_dict = dict()
for i in range(n):
    _, *a_list = map(int, input().split())
    for a in a_list:
        count_dict.setdefault(a - 1, []).append(i + 1)
for i in range(n):
    count_str = " ".join(map(str, count_dict.setdefault(i, [])))
    print(f"{len(count_dict[i])} {count_str}")
