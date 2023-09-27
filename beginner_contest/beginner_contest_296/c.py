import sys


N, X = [int(x) for x in input().split()]
A_list = [int(x) for x in input().split()]

A_list_sorted = sorted(A_list)

align_val = 0
if A_list_sorted[0] < 0:
    align_val = A_list_sorted[0]
    #X = X - A_list_sorted[0]
    #A_list_sorted = [A - A_list_sorted[0] for A in A_list_sorted]

max_index = len(A_list_sorted) - 1
min_index = 0
index = None
index_prev = None

if X == 0:
    print('Yes')
    sys.exit()

while True:
    index = (max_index + min_index) // 2
    if index == index_prev:
        index += 1

    if A_list_sorted[index] >= X and A_list_sorted[index-1] < X:
        break
    if A_list_sorted[index] > X:
        max_index = index
    elif A_list_sorted[index] < X:
        min_index = index
    index_prev = index

A_list_lower = A_list_sorted[:index]
A_list_upper = A_list_sorted[index:]

for A_upper in A_list_upper:
    for A_lower in A_list_lower:
        if A_upper - A_lower == X:
            print('Yes')
            sys.exit()
        if A_upper - A_lower < X:
            break

print('No')
