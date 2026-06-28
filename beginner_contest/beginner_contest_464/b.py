h, w = map(int, input().split())
c_list = list()
for _ in range(h):
    c_list.append(list(input()))
di_list = [[False] * w for _ in range(h)]
for i in range(h):
    all_white = True
    for j in range(w):
        if c_list[i][j] == "#":
            all_white = False
            break
    if not all_white:
        break
    for j in range(w):
        di_list[i][j] = True
for i in range(h - 1, 0, -1):
    all_white = True
    for j in range(w):
        if c_list[i][j] == "#":
            all_white = False
            break
    if not all_white:
        break
    for j in range(w):
        di_list[i][j] = True
for j in range(w):
    all_white = True
    for i in range(h):
        if c_list[i][j] == "#":
            all_white = False
            break
    if not all_white:
        break
    for i in range(h):
        di_list[i][j] = True
for j in range(w - 1, 0, -1):
    all_white = True
    for i in range(h):
        if c_list[i][j] == "#":
            all_white = False
            break
    if not all_white:
        break
    for i in range(h):
        di_list[i][j] = True
answer = ""
for i in range(h):
    line = ""
    for j in range(w):
        if di_list[i][j]:
            continue
        line += c_list[i][j]
    if line != "":
        answer += line + "\n"
print(answer)
