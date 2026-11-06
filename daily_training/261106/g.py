import heapq

n, m = map(int, input().split())
a_list = list(map(int, input().split()))
graph = dict()

for _ in range(m):
    u, v, b = map(int, input().split())
    graph.setdefault(u - 1, list()).append((v - 1, b))
    graph.setdefault(v - 1, list()).append((u - 1, b))

w_list = [-1] * n
heap = [(a_list[0], 0)]

while heap:
    w, v = heapq.heappop(heap)
    if w_list[v] != -1:
        continue
    w_list[v] = w
    for nv, nb in graph[v]:
        if w_list[nv] == -1:
            heapq.heappush(heap, (w + nb + a_list[nv], nv))

print(*w_list[1:])
