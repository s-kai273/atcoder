def check_bingo(mark_list):
    # Check rows and columns
    for i in range(3):
        if all(mark_list[i][j] == 1 for j in range(3)) or all(mark_list[j][i] == 1 for j in range(3)):
            return True

    # Check diagonals
    if all(mark_list[i][i] == 1 for i in range(3)) or all(mark_list[i][2 - i] == 1 for i in range(3)):
        return True

    return False

A_list = [list(map(int, input().split())) for _ in range(3)]
mark_list = [[0] * 3 for _ in range(3)]

N = int(input())
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A_list[i][j] == b:
                mark_list[i][j] = 1

if check_bingo(mark_list):
    print("Yes")
else:
    print("No")
