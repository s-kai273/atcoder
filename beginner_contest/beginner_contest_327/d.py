import sys


N, M = [int(x) for x in input().split()]
A_list = [int(x) for x in input().split()]
B_list = [int(x) for x in input().split()]

group = [[], []]

for i in range(M):
    A = A_list[i]
    B = B_list[i]
    if A in group[0]:
        group[0].append(A)
        group[1].append(B)
    elif A in group[1]:
        group[0].append(B)
        group[1].append(A)
    elif B in group[0]:
        group[0].append(B)
        group[1].append(A)
    elif B in group[1]:
        group[0].append(A)
        group[1].append(B)
    else:
        group[0].append(A)
        group[1].append(B)

for val in range(N):
    if val in group[0] and val in group[1]:
        print('No')
        sys.exit()

print('Yes')
