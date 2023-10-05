N, M = [int(x) for x in input().split()]
A_list = [int(x) for x in input().split()]

last_A_index = None
for i in range(1, N + 1):
    index = None
    if last_A_index is None:
        index = 0
    else:
        for j in range(last_A_index, M):
            if i <= A_list[j]:
                index = j
                break
    A = A_list[index]
    print(A - i)
    last_A_index = index
