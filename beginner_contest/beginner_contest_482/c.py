h, w, n, q = map(int, input().split())
col_count = [0] * h
row_count = [0] * w

for _ in range(n):
    r, c = map(int, input().split())
    col_count[r - 1] += 1
    row_count[c - 1] += 1

col_sum_count = list()
row_sum_count = list()

col_sum = 0
for i in range(h):
    col_sum += col_count[i]
    col_sum_count.append(col_sum)

row_sum = 0
for i in range(w):
    row_sum += row_count[i]
    row_sum_count.append(row_sum)

for _ in range(q):
    query_parts = list(map(int, input().split()))
    answer = None
    if query_parts[0] == 1:
        u = query_parts[1]
        d = query_parts[2]
        answer = (
            col_sum_count[d - 1] - col_sum_count[u - 2]
            if u > 1
            else col_sum_count[d - 1]
        )
    else:
        l = query_parts[1]
        r = query_parts[2]
        answer = (
            row_sum_count[r - 1] - row_sum_count[l - 2]
            if l > 1
            else row_sum_count[r - 1]
        )
    print(answer)
