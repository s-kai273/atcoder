N = int(input())
S = input()

try:
    print(S.index('ABC') + 1)
except ValueError:
    print(-1)
