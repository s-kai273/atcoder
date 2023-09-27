import sys


N = int(input())
S = input()

S_ch_list = list(S)
prev_ch = ''

for ch in S_ch_list:
    if ch == prev_ch:
        print('No')
        sys.exit()
    prev_ch = ch

print('Yes')
