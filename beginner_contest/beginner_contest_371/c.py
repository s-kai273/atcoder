N = int(input())
G = [[0] * N for _ in range(N)]
H = [[0] * N for _ in range(N)]

M_G = int(input())
for _ in range(M_G):
    u, v = map(int, input().split())
    G[u - 1][v - 1] = 1
    G[v - 1][u - 1] = 1

M_H = int(input())
for _ in range(M_H):
    a, b = map(int, input().split())
    H[a - 1][b - 1] = 1
    H[b - 1][a - 1] = 1

cost_list = [[0] * N for _ in range(N)]
for i in range(N - 1):
    A = list(map(int, input().split()))
    for j in range(i + 1, N):
        cost_list[i][j] = A[j - i - 1]
        cost_list[j][i] = A[j - i - 1]

min_cost = float('inf')

import itertools
for perm in itertools.permutations(range(N)):
    cost = 0
    for i in range(N):
        for j in range(i + 1, N):
            if G[i][j] != H[perm[i]][perm[j]]:
                cost += cost_list[perm[i]][perm[j]]
    min_cost = min(min_cost, cost)

print(min_cost)