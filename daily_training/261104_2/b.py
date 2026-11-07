n = int(input())
h_list = list(map(int, input().split()))

max_i = 0
for i in range(n):
    if h_list[i] > h_list[max_i]:
        max_i = i

print(max_i + 1)
