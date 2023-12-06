M, D = [int(x) for x in input().split()]
y, m, d = [int(x) for x in input().split()]

new_d = d + 1 if d < D else 1
new_m = m if new_d != 1 else (m + 1 if m < M else 1)
new_y = y if new_m != 1 else y + 1

print("{} {} {}".format(new_y, new_m, new_d))
