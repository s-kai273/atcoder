N = int(input())
C_list = list()
A_list = list()

for i in range(N):
    C = int(input())
    A_vals = [int(a) for a in input().split()]
    C_list.append(C)
    A_list.append(A_vals)

X = int(input())

min_C = 37
for i in range(N):
    if X in A_list[i] and min_C >= C_list[i]:
        min_C = C_list[i]

target_list = list()
for i in range(N):
    if X in A_list[i] and C_list[i] == min_C:
        target_list.append(str(i + 1))

print(len(target_list))
print(' '.join(target_list))
