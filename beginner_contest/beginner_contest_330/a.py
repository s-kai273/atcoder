N, L = [int(x) for x in input().split()]
A_list = [int(x) for x in input().split()]

answer = 0

for A in A_list:
    if A >= L:
        answer += 1

print(answer)
