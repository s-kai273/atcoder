N = int(input())
D_list = [int(x) for x in input().split()]

answer = 0

for i in range(N):
    x = (i + 1) // 10
    y = (i + 1) - 10 * x
    if x == 0 or x == y:
        for d in range(1, D_list[i] + 1):
            if y == d:
                answer += 1
            if 10 * y + y == d:
                answer += 1

print(answer)
