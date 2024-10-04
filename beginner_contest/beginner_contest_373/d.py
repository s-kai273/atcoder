N, M = map(int, input().split())

connected_dict = dict()
for i in range(N):
    connected_dict[i] = set()

x = [None] * N

for _ in range(M):
    u, v, w = map(int, input().split())

    connected_dict[u - 1].add((v - 1, w))
    connected_dict[v - 1].add((u - 1, -w))

from collections import deque
Q = deque()

for i in range(N):
    if x[i] is not None:
        continue

    x[i] = 0
    Q.append(i)

    while Q:
        u = Q.popleft()
        for v, w in connected_dict[u]:
            if x[v] is None:
                x[v] = x[u] + w
                Q.append(v)
            else:
                if x[v] != x[u] + w:
                    pass

for i in range(N):
    x[i] = str(x[i])

print(' '.join(x))
