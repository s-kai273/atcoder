n = int(input())
lr_list = list()
min_score = 0
min_score_indexes = set()
for i in range(n):
    l, r = map(int, input().split())
    if l * r > 0:
        min_score += r if abs(l) > abs(r) else l
        min_score_indexes.add(i)
    lr_list.append((l, r))

x_list = list()
for i in range(n):
    if i in min_score_indexes:
        l, r = lr_list[i][0], lr_list[i][1]
        x = r if abs(l) > abs(r) else l
        x_list.append(x)
        continue
    if min_score == 0:
        x_list.append(0)
    elif min_score > 0:
        if min_score + lr_list[i][0] > 0:
            min_score += lr_list[i][0]
            x_list.append(lr_list[i][0])
        else:
            x_list.append(-min_score)
            min_score = 0
    else:
        if min_score + lr_list[i][1] < 0:
            min_score += lr_list[i][1]
            x_list.append(lr_list[i][1])
        else:
            x_list.append(-min_score)
            min_score = 0

if min_score == 0:
    print("Yes")
    print(*x_list)
else:
    print("No")
