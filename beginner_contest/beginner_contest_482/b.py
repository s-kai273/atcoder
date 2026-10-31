s_list = list()

for _ in range(5):
    s_list.append(list(input()))

min_count = 5

for i in range(5):
    count = 0
    for j in range(5):
        if s_list[i][j] != "o":
            count += 1
    min_count = min(min_count, count)

for i in range(5):
    count = 0
    for j in range(5):
        if s_list[j][i] != "o":
            count += 1
    min_count = min(min_count, count)

count = 0
for i in range(5):
    if s_list[i][i] != "o":
        count += 1
min_count = min(min_count, count)

count = 0
for i in range(5):
    if s_list[i][4 - i] != "o":
        count += 1
min_count = min(min_count, count)

print(min_count)
