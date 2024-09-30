N, L = map(int, input().split())
x_list = list(map(int, input().split()))
T1, T2, T3 = map(int, input().split())

min_time_list = [0] * (L + 1)
for x in x_list:
    min_time_list[x] = T3

min_time_list[0] = 0
min_time_list[1] += T1

for i in range(2, L + 1):
    time1 = min_time_list[i - 1] + T1
    time2 = min_time_list[i - 2] + T1 + T2 if i >= 2 else float('inf')
    time3 = min_time_list[i - 4] + T1 + 3 * T2 if i >= 4 else float('inf')
    min_time_list[i] += min(time1, time2, time3)

answer = min_time_list[L]
for i in [L - 3, L - 2, L - 1]:
    if i >= 0:
        answer = min(answer, min_time_list[i] + T1 // 2 + T2 * (L - i) - T2 // 2)

print(answer)