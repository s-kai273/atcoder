import sys


N, D = [int(x) for x in input().split()]
T_list = [int(t) for t in input().split()]

for i in range(N - 1):
    if T_list[i+1] - T_list[i] <= D:
        print(T_list[i+1])
        sys.exit()
print(-1)
