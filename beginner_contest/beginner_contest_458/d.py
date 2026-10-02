import heapq

x = int(input())
q = int(input())
small_list = list()
large_list = list()

cur_med = x

for _ in range(q):
    a, b = map(int, input().split())
    if a > cur_med and b > cur_med:
        heapq.heappush(small_list, -1 * cur_med)
        heapq.heappush(large_list, a)
        heapq.heappush(large_list, b)
        cur_med = heapq.heappop(large_list)
    elif a < cur_med and b < cur_med:
        heapq.heappush(large_list, cur_med)
        heapq.heappush(small_list, -1 * a)
        heapq.heappush(small_list, -1 * b)
        cur_med = -1 * heapq.heappop(small_list)
    else:
        if a > b:
            heapq.heappush(large_list, a)
            heapq.heappush(small_list, -1 * b)
        else:
            heapq.heappush(large_list, b)
            heapq.heappush(small_list, -1 * a)
    print(cur_med)
