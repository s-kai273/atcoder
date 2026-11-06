import heapq

q = int(input())
heap = list()

for i in range(q):
    cmd, h = map(int, input().split())
    if cmd == 1:
        heapq.heappush(heap, h)
    else:
        while heap and heap[0] <= h:
            heapq.heappop(heap)
    print(len(heap))
