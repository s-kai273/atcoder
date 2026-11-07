n = int(input())
h_list = list(map(int, input().split()))

answer = 1

for k in range(1, n):
    for start in range(k):
        count = 0
        prev = h_list[start]
        for i in range(start, n, k):
            if h_list[i] != prev:
                count = 0
            count += 1
            prev = h_list[i]
            if count > answer:
                answer = count

print(answer)
