N, X, Y = map(int, input().split())

dist = [[-1] * 403 for _ in range(403)]
base = 201

for _ in range(N):
    x, y = map(int, input().split())
    dist[y + base][x + base] = -2

from collections import deque

Q = deque()
Q.append((0 + base, 0 + base))
dist[0 + base][0 + base] = 0

while len(Q) > 0:
    x, y = Q.popleft()
    for nx, ny in [(x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x + 1, y), (x - 1, y), (x, y - 1)]:
        if nx > 402 or ny > 402 or nx < 0 or ny < 0:
            continue
        if dist[ny][nx] == -2:
            continue
        if dist[ny][nx] != -1:
            continue
        Q.append((nx, ny))
        dist[ny][nx] = dist[y][x] + 1

print(dist[Y + base][X + base])