N, M = map(int, input().split())
has_taro = [False] * N

for _ in range(M):
    A, B = input().split()
    if B == "F":
        print("No")
    elif has_taro[int(A)-1]:
        print("No")
    else:
        print("Yes")
        has_taro[int(A)-1] = True