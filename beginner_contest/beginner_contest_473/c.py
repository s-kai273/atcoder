n, k = map(int, input().split())
a_list = list(map(int, input().split()))
counter = dict()
max_count = 0

for a in a_list:
    counter[a] = counter.get(a, 0) + 1
    if counter[a] > max_count:
        max_count = counter[a]

answer = 0
for count in counter.values():
    if count >= max_count - 1:
        answer += 1
print(answer)
