H, W = [int(x) for x in input().split()]
S_list = [input() for _ in range(H)]

for S in S_list:
    print(S.replace('TT', 'PC'))
