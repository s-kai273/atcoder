n = int(input())
a_list = [[-1] * n for _ in range(n)]

a_list[0][(n - 1) // 2] = 1
k = 1
pr = 0
pc = (n - 1) // 2

for i in range(n**2 - 1):
    if a_list[(pr - 1) % n][(pc + 1) % n] == -1:
        a_list[(pr - 1) % n][(pc + 1) % n] = k + 1
        pr = (pr - 1) % n
        pc = (pc + 1) % n
    else:
        a_list[(pr + 1) % n][pc] = k + 1
        pr = (pr + 1) % n
        pc = pc
    k += 1

for a in a_list:
    print(*a)
