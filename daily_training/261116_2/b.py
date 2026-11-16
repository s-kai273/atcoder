x, y = map(int, input().split())
if x > y:
    print(0)
else:
    print((y - x - 1) // 10 + 1)
