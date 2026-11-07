import heapq

n, m = map(int, input().split())
a_list = list(map(int, input().split()))
graph = [list() for _ in range(n)]

for _ in range(m):
    u, v, b = map(int, input().split())
    graph[u - 1].append((v - 1, b))
    graph[v - 1].append((u - 1, b))

w_list = [float("INF")] * n
w_list[0] = a_list[0]
heap = [(w_list[0], 0)]

while heap:
    w, v = heapq.heappop(heap)
    if w_list[v] < w:
        continue
    w_list[v] = w
    for nv, nb in graph[v]:
        nw = w + nb + a_list[nv]
        if w_list[nv] > nw:
            w_list[nv] = nw
            heapq.heappush(heap, (w_list[nv], nv))

print(*w_list[1:])
