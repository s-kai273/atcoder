N = int(input())
C = list(map(int, input().split()))
Q = int(input())
answer = 0

min_s_c = float('inf')
min_c = float('inf')
s = 0
z = 0

for i in range(N):
    if i % 2 == 0:
        min_s_c = min(min_s_c, C[i])
    min_c = min(min_c, C[i])

for _ in range(Q):
    S = list(map(int, input().split()))
    if S[0] == 1:
        x = S[1] - 1
        a = S[2]
        available = C[x] - s - z if x % 2 == 0 else C[x] - z
        if available >= a:
            C[x] -= a
            if x % 2 == 0:
                min_s_c = min(min_s_c, C[x])
            min_c = min(min_c, C[x])
            answer += a
    elif S[0] == 2:
        a = S[1]
        if min_s_c - s - z >= a:
            s += a
            answer += a * (N // 2 + N % 2)
    elif S[0] == 3:
        a = S[1]
        if min(min_s_c - s - z, min_c - z) >= a:
            z += a
            answer += a * N
print(answer)
