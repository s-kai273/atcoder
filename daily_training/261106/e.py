import heapq

q = int(input())
q_list = [tuple(map(int, input().split())) for _ in range(q)]
heap = list()

for i in range(q):
    cmd, h = q_list[i]
    if cmd == 1:
        heapq.heappush(heap, h)
    else:
        while heap and heap[0] <= h:
            heapq.heappop(heap)
    print(len(heap))
