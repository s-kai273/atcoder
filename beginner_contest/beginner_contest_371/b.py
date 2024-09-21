N, M = map(int, input().split())
has_taro = [False] * N

for _ in range(M):
    A, B = input().split()
    A = int(A) - 1
    if B == "F" or has_taro[A]:
        print("No")
    else:
        print("Yes")
        has_taro[A] = True