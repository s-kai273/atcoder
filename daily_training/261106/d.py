n, a = map(int, input().split())
t_list = list(map(int, input().split())) + [0]

et = t_list[0]

for i in range(1, n + 1):
    et += a
    print(et)
    if et < t_list[i]:
        et = t_list[i]
