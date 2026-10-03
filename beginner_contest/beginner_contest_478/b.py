n, v = map(int, input().split())
w_list = list(map(int, input().split()))

answer = 0
for i in range(len(w_list)):
    for j in range(i + 1, len(w_list)):
        for k in range(j + 1, len(w_list)):
            if i + j + k + 3 > v:
                continue
            answer = max(answer, w_list[i] + w_list[j] + w_list[k])
print(answer)
