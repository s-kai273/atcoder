n = int(input())
answer = 0
count_dict = dict()
for _ in range(n):
    s = input().lower()
    count_dict[s] = count_dict.get(s, 0) + 1
    if count_dict[s] > answer:
        answer = count_dict[s]
print(answer)
