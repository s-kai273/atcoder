import sys


N = int(input())
S = input()

for i in range(len(S)):
    if i == len(S) - 1:
        break
    if (S[i] == 'a' and S[i + 1] == 'b') or (S[i] == 'b' and S[i + 1] == 'a'):
        print('Yes')
        sys.exit()

print('No')
