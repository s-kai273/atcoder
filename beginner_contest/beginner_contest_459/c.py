n, q = map(int, input().split())
block_dict = dict()
count_dict = dict()
count_dict[0] = n
dec_count = 0
for _ in range(q):
    q_parts = list(map(int, input().split()))
    if q_parts[0] == 1:
        x = q_parts[1]
        block_dict[x - 1] = block_dict.get(x - 1, 0) + 1
        count = block_dict[x - 1]
        count_dict[count] = count_dict.get(count, 0) + 1
        if count_dict.get(dec_count + 1, 0) == n:
            dec_count += 1
    else:
        y = q_parts[1]
        print(count_dict.get(y + dec_count, 0))
