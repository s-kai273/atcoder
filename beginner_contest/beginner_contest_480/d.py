n, q = map(int, input().split())
a_list = list(map(int, input().split()))

b_list = list()
for i in range(n):
    b_list.extend(a_list[: i + 1])

b_sum_list = list()
for i in range(len(b_list)):
    if i == 0:
        b_sum_list.append(b_list[i])
    else:
        b_sum_list.append(b_sum_list[i - 1] + b_list[i])

for _ in range(q):
    l, r = map(int, input().split())
    il, ir = 0, 0
    for i in range(n):

    if l == 1:
        print(b_sum_list[r - 1])
    else:
        print(b_sum_list[r - 1] - b_sum_list[l - 2])
