from itertools import permutations

count_list = list()
for i in range(3):
    a_list = list(map(int, input().split()))
    count_list.append(dict())
    for a in a_list:
        count_list[i][a] = count_list[i].get(a, 0) + 1
count = 0
for i, j, k in permutations([4, 5, 6]):
    count += count_list[0].get(i, 0) * count_list[1].get(j, 0) * count_list[2].get(k, 0)
print(count / (6 * 6 * 6))

