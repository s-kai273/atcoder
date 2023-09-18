S = input()

try:
    B_i1 = S.index('B')
    B_i2 = S.index('B', B_i1 + 1)

    R_i1 = S.index('R')
    R_i2 = S.index('R', R_i1 + 1)

    K_i = S.index('K')

    if (B_i1 + B_i2) % 2 == 1 and R_i1 < K_i and K_i < R_i2:
        print('Yes')
    else:
        print('No')
except ValueError:
    print('No')
