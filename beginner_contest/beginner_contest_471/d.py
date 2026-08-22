import heapq

q, v = map(int, input().split())
battery_dict = dict()
output_time_list = set()
time_list = list()
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        battery_dict[query[1]] = query[2]
        time_list.append(query[1])
    else:
        output_time_list.add(query[1])
        time_list.append(query[1])
time_list.sort()
max_heap = list()

for t in time_list:
    if t in battery_dict:
        heapq.heappush(max_heap, -1 * (battery_dict[t] - t))
    if t in output_time_list:
        max_battery = min(v, -1 * heapq.heappop(max_heap) + t if max_heap else -1)
        print(max_battery)
