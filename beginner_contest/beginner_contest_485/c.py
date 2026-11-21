from collections import deque

n = int(input())
c_list = list(map(int, input().split()))

dist_list = list()
queue = deque([(0, c_list[0], float("inf"))])

for i in range(1, n):
    c = c_list[i]

    while queue and queue[0][1] != c:
        target = queue.popleft()
        dist = min(i - target[0], target[2])
        dist_list.append(dist)

    if queue:
        if queue[0][2] == float("inf"):
            queue.append((i, c, float("inf")))
        else:
            queue.append((i, c, queue[-1][2] + 1))
    else:
        queue.append((i, c, 1))

for i, c, dist in queue:
    dist_list.append(dist)

print(*dist_list)
