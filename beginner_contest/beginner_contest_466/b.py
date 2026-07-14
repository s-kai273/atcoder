n, m = map(int, input().split())
c_max_dict = dict()
for _ in range(n):
    c, s = map(int, input().split())
    c_max_dict[c] = max(c_max_dict.get(c, -1), s)
print(" ".join([str(c_max_dict.get(k + 1, -1)) for k in range(m)]))
