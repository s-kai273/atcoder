A_list = list()
mark_list = [[0] * 3 for _ in range(3)] 

for i in range(3):
    A_list.append(list(map(int, input().split())))

N = int(input())
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A_list[i][j] == b:
                mark_list[i][j] = 1

result = False
for i in range(3):
    if mark_list[i][0] == mark_list[i][1] == mark_list[i][2] == 1:
        result = True
    if mark_list[0][i] == mark_list[1][i] == mark_list[2][i] == 1:
        result = True
if mark_list[0][0] == mark_list[1][1] == mark_list[2][2] == 1:
    result = True
if mark_list[0][2] == mark_list[1][1] == mark_list[2][0] == 1:
    result = True

if result:
    print("Yes")
else:
    print("No")
