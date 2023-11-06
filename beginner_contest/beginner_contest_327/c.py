import sys


A_list = list()
for _ in range(9):
    A_list.append([int(a) for a in input().split()])

for i in range(9):
    check_list = [0] * 9
    for j in range(9):
        a = A_list[i][j]
        check_list[a - 1] = 1
    if 0 in check_list:
        print('No')
        sys.exit()

for j in range(9):
    check_list = [0] * 9
    for i in range(9):
        a = A_list[i][j]
        check_list[a - 1] = 1
    if 0 in check_list:
        print('No')
        sys.exit()

for offset_i in [0, 3, 6]:
    for offset_j in [0, 3, 6]:
        check_list = [0] * 9
        for i in range(3):
            for j in range(3):
                a = A_list[i + offset_i][j + offset_j]
                check_list[a - 1] = 1
        if 0 in check_list:
            print('No')
            sys.exit()

print('Yes')
