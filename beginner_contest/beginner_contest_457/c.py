n, k = map(int, input().split())
l_list = list()
a_list = list()
for _ in range(n):
    l, *arr = map(int, input().split())
    l_list.append(l)
    a_list.append(arr)
c_list = list(map(int, input().split()))
count = 0
target_i = -1
delta_i = -1
for i in range(n):
    count += l_list[i] * c_list[i]
    if count >= k:
        target_i = i
        delta_i = (k - count + l_list[i] * c_list[i]) % l_list[i]
        delta_i = l_list[i] if delta_i == 0 else delta_i
        break
print(a_list[target_i][delta_i - 1])
