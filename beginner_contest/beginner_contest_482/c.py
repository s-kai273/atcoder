import bisect

h, w, n, q = map(int, input().split())
r_list = list()
c_list = list()

for _ in range(n):
    r, c = map(int, input().split())
    r_list.append(r)
    c_list.append(c)

r_list.sort()
c_list.sort()

for _ in range(q):
    q_parts = list(map(int, input().split()))
    if q_parts[0] == 1:
        u = q_parts[1]
        d = q_parts[2]
        print(bisect.bisect_right(r_list, d) - bisect.bisect_left(r_list, u))
    else:
        l = q_parts[1]
        r = q_parts[2]
        print(bisect.bisect_right(c_list, r) - bisect.bisect_left(c_list, l))
