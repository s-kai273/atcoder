import sys

n, m = map(int, input().split())
s_list = [input() for _ in range(n)]

target = "x" * m
for i, s in enumerate(s_list):
    if s == target:
        print(f"Faucet {i + 1}")
        sys.exit()

target = "x" * n
for j in range(m):
    cur_s = list()
    for i in range(n):
        cur_s.append(s_list[i][j])
    if "".join(cur_s) == target:
        print(f"Drain {j + 1}")
        sys.exit()
