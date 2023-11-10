N, M = [int(x) for x in input().split()]
A_list = sorted([int(x) for x in input().split()])

answer = 0
st_i = 0
for b_i in range(N):
    for i in range(st_i, N):
        if A_list[i] - A_list[b_i] >= M:
            answer = i - b_i if answer < i - b_i else answer
            st_i = i - 1
            break
        if i == N - 1:
            answer = i - b_i + 1 if answer < i - b_i + 1 else answer
            st_i = N - 1
    if st_i == N - 1:
        break

print(answer)
