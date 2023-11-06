import sys


B = int(input())

for A in range(1, 20):
    A_A = A ** A
    if A_A == B:
        print(A)
        sys.exit()
    if A_A > B:
        break

print(-1)
