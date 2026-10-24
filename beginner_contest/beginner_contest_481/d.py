from collections import deque

n, m, s, t = map(int, input().split())
visited = set()

adj_list = [list() for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)

for adj in adj_list:
    adj.sort()

min_fuel = -1
queue = deque([(s, 0)])

while queue:
    v, fuel = queue.popleft()
    if v == t:
        min_fuel = fuel
        break
    if v in visited:
        continue
    visited.add(v)
    for i, next in enumerate(adj_list[v]):
        if i == 0:
            queue.appendleft((next, fuel))
        else:
            queue.append((next, fuel + 1))
print(min_fuel)
