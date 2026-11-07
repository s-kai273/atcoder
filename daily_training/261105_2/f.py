n, q = map(int, input().split())
a_list = [i + 1 for i in range(n)]

head = 0

for _ in range(q):
    q_parts = list(map(int, input().split()))
    if q_parts[0] == 1:
        p = q_parts[1]
        x = q_parts[2]
        i = head + p - 1 if head + p - 1 < n else (head + p - 1) % n
        a_list[i] = x
    elif q_parts[0] == 2:
        p = q_parts[1]
        i = head + p - 1 if head + p - 1 < n else (head + p - 1) % n
        print(a_list[i])
    else:
        k = q_parts[1]
        head = head + k if head + k < n else (head + k) % n
