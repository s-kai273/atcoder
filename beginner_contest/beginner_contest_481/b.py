n, k = map(int, input().split())
a_list = list(map(int, input().split()))

count = 0
for i in range(1, n):
    if a_list[i - 1] <= k < a_list[i] or a_list[i] < k <= a_list[i - 1]:
        count += 1
if a_list[-1] == k:
    count += 1
print(count)
