points = [tuple(map(int, input().split())) for _ in range(4)]

answer = "Yes"

for i in range(4):
    x, y, z = points[i], points[(i + 1) % 4], points[(i + 2) % 4]
    av = (x[0] - y[0], x[1] - y[1])
    bv = (z[0] - y[0], z[1] - y[1])
    cross = av[0] * bv[1] - av[1] * bv[0]
    if cross > 0:
        answer = "No"
        break

print(answer)
