n, k, t = map(int, input().split())
a_list = list(map(int, input().split()))
a_list.sort()

count = 0
current = 0
if a_list[0] == 0:
    current = k
elif a_list[0] > t:
    print((t - 1) // k + 1)
    exit()
else:
    count += (a_list[0] - 1) // k + 1
    current = a_list[0] + k

for i in range(1, n):
    if a_list[i] == a_list[i - 1]:
        continue
    target = min(a_list[i], t)
    if current < target:
        count += (target - current - 1) // k + 1
    if current >= t:
        print(count)
        exit()
    current = target + k
if current < t:
    count += (t - current - 1) // k + 1
print(count)
