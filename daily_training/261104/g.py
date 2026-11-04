n = int(input())

divider = 998244353

r = 0
for i in range(n):
    r += (n * (10**i)) % divider
    if r >= divider:
        r %= divider

print(r)
