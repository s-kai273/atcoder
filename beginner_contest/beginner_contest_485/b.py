n, m = map(int, input().split())
s_list = [input() for _ in range(n)]

target = "x" * m
for i, s in enumerate(s_list):
    if s == target:
        print(f"Faucet {i + 1}")
        break

else:
    for j in range(m):
        if s_list[0][j] == "x":
            print(f"Drain {j + 1}")
