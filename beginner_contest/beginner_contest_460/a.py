n, m = map(int, input().split())
answer = 0
while True:
    m = n % m
    answer += 1
    if m == 0:
        break
print(answer)
