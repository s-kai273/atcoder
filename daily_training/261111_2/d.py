n = int(input())
a_list = list()

for _ in range(n):
    a_list.append(list(map(int, input().split())))

answer = a_list[0][0]

for j in range(1, n):
    i = answer - 1
    if i >= j:
        answer = a_list[i][j]
    else:
        answer = a_list[j][i]

print(answer)
