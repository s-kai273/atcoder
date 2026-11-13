n, m = map(int, input().split())
d = m // n
r = m % n
for i in range(1, n + 1):
    print(d + (1 if i <= r else 0))
