N, X = [int(x) for x in input().split()]
S_list = [int(x) for x in input().split()]

answer = 0

for S in S_list:
    if S <= X:
        answer += S

print(answer)
