N, M = [int(x) for x in input().split()]
S = input()
C_list = [int(x) for x in input().split()]

color_group_list = [[] for _ in range(M)]

for i in range(N):
    C = C_list[i]
    color_group_list[C - 1].append(i)

new_color_dict = dict()

for color_index_list in color_group_list:
    for i in range(len(color_index_list)):
        index = color_index_list[i]
        if i == 0:
            new_color_dict[index] = color_index_list[-1]
        else:
            new_color_dict[index] = color_index_list[i - 1]

answer_char_list = [S[new_color_dict[i]] for i in range(len(S))]

print(''.join(answer_char_list))
