import bisect

h, w, n, q = map(int, input().split())
col_count = {0: 0}
row_count = {0: 0}

for _ in range(n):
    r, c = map(int, input().split())
    col_count[r] = col_count.get(r, 0) + 1
    row_count[c] = row_count.get(c, 0) + 1

cols = [0] + sorted(col_count.keys())
rows = [0] + sorted(row_count.keys())

col_sum_count = dict()
row_sum_count = dict()

col_sum = 0
for c in cols:
    col_sum += col_count[c]
    col_sum_count[c] = col_sum

row_sum = 0
for r in rows:
    row_sum += row_count[r]
    row_sum_count[r] = row_sum

for _ in range(q):
    q_parts = list(map(int, input().split()))
    if q_parts[0] == 1:
        u = q_parts[1]
        d = q_parts[2]
        cr = (
            bisect.bisect_left(cols, d)
            if d in col_count.keys()
            else bisect.bisect_left(cols, d) - 1
        )
        cl = bisect.bisect_left(cols, u) - 1 if u > 1 else 0
        print(col_sum_count[cols[cr]] - col_sum_count[cols[cl]])
    else:
        l = q_parts[1]
        r = q_parts[2]
        rr = (
            bisect.bisect_left(rows, r)
            if r in row_count.keys()
            else bisect.bisect_left(rows, r) - 1
        )
        rl = bisect.bisect_left(rows, l) - 1 if l > 1 else 0
        print(row_sum_count[rows[rr]] - row_sum_count[rows[rl]])
