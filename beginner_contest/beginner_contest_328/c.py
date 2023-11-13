N, Q = [int(x) for x in input().split()]
S = input()

X_list = [0] * (N - 1)

for i in range(N - 1):
    if S[i] == S[i + 1]:
        X_list[i] = 1

for _ in range(Q):
    l, r = [int(x) for x in input().split()]
    print(sum(X_list[l - 1:r - 1]))
