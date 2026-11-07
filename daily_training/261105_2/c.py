n, p = map(int, input().split())
a_list = list(map(int, input().split()))

count = 0
for a in a_list:
    if a < p:
        count += 1

print(count)
