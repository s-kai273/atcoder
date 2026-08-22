from collections import deque

n = int(input())
a_list = list(map(int, input().split()))
a_list.sort()

neg_queue = deque()
pos_queue = deque()

for a in a_list:
    if a < 0:
        neg_queue.append(a)
    else:
        pos_queue.append(a)

answer = 0
current = 0
while neg_queue and pos_queue:
    if abs(neg_queue[-1] - current) <= abs(pos_queue[0] - current):
        answer += abs(neg_queue[-1] - current)
        current = neg_queue.pop()
    else:
        answer += abs(pos_queue[0] - current)
        current = pos_queue.popleft()
if neg_queue or pos_queue:
    rem_queue = neg_queue if neg_queue else pos_queue
    answer += (
        abs(rem_queue[0] - current)
        if abs(rem_queue[0] - current) > abs(rem_queue[-1] - current)
        else abs(rem_queue[-1] - current)
    )
print(answer)
