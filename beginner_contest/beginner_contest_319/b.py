N = int(input())

answer = ''
for i in range(N + 1):
    min_divisor = '-'
    for j in range(1, 10):
        if N % j == 0 and i % (N / j) == 0:
            min_divisor = str(j)
            break
    answer += min_divisor

print(answer)
