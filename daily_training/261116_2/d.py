n = int(input())
area_set = set()

for _ in range(n):
    a, b, c, d = map(int, input().split())
    for i in range(a, b):
        for j in range(c, d):
            area_set.add((i, j))

print(len(area_set))
