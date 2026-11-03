from itertools import permutations

count_dict = {i: [0] * 3 for i in range(1, 7)}

for i in range(3):
    a_list = list(map(int, input().split()))
    for a in a_list:
        count_dict[a][i] += 1

count = 0
for a, b, c in permutations([4, 5, 6]):
    count += count_dict[a][0] * count_dict[b][1] * count_dict[c][2]
print(count / 6**3)
