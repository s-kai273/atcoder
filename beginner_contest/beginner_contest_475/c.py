# C1 5 C2 2 C3 4 C4 1 C5 6 C6
# C1 2 C2 3 C3 4 C4 4 C5 3 C6 5 C7 1 C8

n, s, l = map(int, input().split())
a_list = list(map(int, input().split()))

r_dist = 0
r_city = 1
for i in range(s - 1, n - 1):
    if r_dist + a_list[i] > l:
        break
    r_dist += a_list[i]
    r_city += 1
for i in range(s - 2, -1, -1):
    if r_dist + a_list[i] * 2 > l:
        break
    r_dist += a_list[i] * 2
    r_city += 1

l_dist = 0
l_city = 1
for i in range(s - 2, -1, -1):
    if l_dist + a_list[i] > l:
        break
    l_dist += a_list[i]
    l_city += 1
for i in range(s - 1, n - 1):
    if l_dist + a_list[i] * 2 > l:
        break
    l_dist += a_list[i] * 2
    l_city += 1

print(max(r_city, l_city))
