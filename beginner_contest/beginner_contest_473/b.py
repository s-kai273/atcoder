n = int(input())
a_list = list(map(int, input().split()))

seen = set()
answer = 0
for a in a_list:
    if a not in seen:
        answer += a
        seen.add(a)
    else:
        answer -= a
        seen.remove(a)
print(answer)
