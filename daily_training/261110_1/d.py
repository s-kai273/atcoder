n = int(input())
s_list = list()

for _ in range(n):
    s_list.append(input())

s_list.sort(key=lambda s: len(s))

print("".join(s_list))
