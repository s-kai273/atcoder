n, k = map(int, input().split())
a_list = list(map(int, input().split()))
sorted_a_list = sorted(a_list)

answer = "Yes"
target_s = n - k
for i in range(n - k + 1):
    if a_list[i] != sorted_a_list[i]:
        target_s = i
        break
for i in range(target_s + k, n):
    if a_list[i] != sorted_a_list[i]:
        answer = "No"
        break
print(answer)
