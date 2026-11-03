from collections import deque

queue = deque()

q = int(input())
for _ in range(q):
    q_parts = list(map(int, input().split()))
    if q_parts[0] == 1:
        c = q_parts[1]
        x = q_parts[2]
        queue.append((c, x))
    else:
        k = q_parts[1]
        sum = 0
        while True:
            c, x = queue.popleft()
            if k > c:
                k -= c
                sum += c * x
            else:
                sum += k * x
                queue.appendleft((c - k, x))
                break
        print(sum)
