h, w = map(int, input().split())
for i in range(h):
    count_list = list()
    for j in range(w):
        count = 0
        if h == 1:
            count += 0
        elif i == 0 or i == h - 1:
            count += 1
        else:
            count += 2
        if w == 1:
            count += 0
        elif j == 0 or j == w - 1:
            count += 1
        else:
            count += 2
        count_list.append(str(count))
    print(" ".join(count_list))
