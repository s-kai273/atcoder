n = int(input())
lr_list = list()
min_sum = 0
max_sum = 0

for _ in range(n):
    l, r = map(int, input().split())
    min_sum += l
    max_sum += r
    lr_list.append((l, r))

if min_sum > 0 or max_sum < 0:
    print("No")
else:
    x_list = list()
    for l, r in lr_list:
        if min_sum == 0:
            x_list.append(l)
            continue

        if min_sum + (r - l) < 0:
            x_list.append(r)
            min_sum += r - l
        else:
            x_list.append(l - min_sum)
            min_sum = 0
    print("Yes")
    print(*x_list)
