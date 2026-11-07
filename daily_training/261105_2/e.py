import math

a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())
d1, d2 = map(int, input().split())

answer = "Yes"

for x1, x2, y1, y2, z1, z2 in [
    (a1, a2, b1, b2, c1, c2),
    (b1, b2, c1, c2, d1, d2),
    (c1, c2, d1, d2, a1, a2),
    (d1, d2, a1, a2, b1, b2),
]:
    av = (x1 - y1, x2 - y2)
    bv = (z1 - y1, z2 - y2)
    sin = (av[0] * bv[1] - av[1] * bv[0]) / (
        math.sqrt(av[0] ** 2 + av[1] ** 2) * math.sqrt(bv[0] ** 2 + bv[1] ** 2)
    )
    print(sin)
    if sin > 0:
        answer = "No"
        break

print(answer)
