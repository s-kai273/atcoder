n = int(input())
ypoint_list = [0] * n
for _ in range(n):
    x, y = map(int, input().split())
    ypoint_list[x - 1] = y
answer = 0
min_y = ypoint_list[0]
for x in range(n):
    y = ypoint_list[x]
    if y <= min_y:
        answer += 1
        min_y = y
print(answer)
