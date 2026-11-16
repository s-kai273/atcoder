n, q = map(int, input().split())
s = input()

sum_list = [0]

cur_dup_sum = 0
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        cur_dup_sum += 1
    sum_list.append(cur_dup_sum)

for i in range(q):
    l, r = map(int, input().split())
    print(sum_list[r - 1] - sum_list[l - 1])
