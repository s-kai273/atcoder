n, m = map(int, input().split())
q = m // n
r = m % n
for i in range(n):
    if i + 1 > r:
        print(q)
    else:
        print(q + 1)
