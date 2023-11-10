N = int(input())
answer = None

for i in range(N, 920):
    x = i  // 100
    y = (i - x * 100) // 10
    z = i - (x * 100) - (y * 10)
    if x * y == z:
        answer = i
        break

print(answer)
