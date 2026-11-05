r, c = map(int, input().split())
a_list = list()
for _ in range(2):
    a_list.append(list(map(int, input().split())))
print(a_list[r - 1][c - 1])
