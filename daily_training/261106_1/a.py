n, x = map(int, input().split())
p_list = list(map(int, input().split()))
k = -1

for i in range(n):
    if p_list[i] == x:
        k = i + 1

print(k)
