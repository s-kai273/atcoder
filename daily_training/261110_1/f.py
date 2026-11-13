n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_max = a_list[0]
b_max = b_list[0]

for i in range(n):
    a_max = max(a_max, a_list[i])
    b_max = max(b_max, b_list[i])

print(a_max + b_max)
