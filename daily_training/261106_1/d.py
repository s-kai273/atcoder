n, m = map(int, input().split())
a_list = list(map(int, input().split()))

num_set = set()
ti = n

for i in range(n):
    a = a_list[i]
    if a <= m and a not in num_set:
        num_set.add(a_list[i])
        if len(num_set) == m:
            ti = i
            break

print(n - ti)
