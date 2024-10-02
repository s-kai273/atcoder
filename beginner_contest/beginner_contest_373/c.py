N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_A = A[0]
max_B = B[0]

for i in range(1, N):
    max_A = max(max_A, A[i])
    max_B = max(max_B, B[i])

print(max_A + max_B)